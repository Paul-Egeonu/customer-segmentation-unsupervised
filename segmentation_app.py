import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# =========================
# Step 1: Load raw dataset
# =========================
RAW_DATA_PATH = "online_retail_II.csv"
PROCESSED_DATA_PATH = "customer_aggregates_with_clusters.csv"

@st.cache_data
def preprocess_and_cluster():
    df = pd.read_csv(RAW_DATA_PATH)

    # --- Step 2: Cleaning ---
    df = df.dropna(subset=["Customer ID"])  # drop null IDs
    df = df[df["Quantity"] > 0]             # remove cancellations/returns
    df = df[df["Price"] > 0]

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # --- Step 3: Feature engineering ---
    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    cust_agg = df.groupby("Customer ID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,   # Recency
        "Invoice": "nunique",                                     # Frequency
        "Quantity": "sum",                                        # Basket size proxy
        "Price": "sum",                                           # Monetary value
        "StockCode": "nunique"                                    # Distinct products
    }).reset_index()

    cust_agg.rename(columns={
        "InvoiceDate": "recency_days",
        "Invoice": "frequency",
        "Quantity": "total_quantity",
        "Price": "monetary",
        "StockCode": "distinct_products"
    }, inplace=True)

    cust_agg["avg_basket"] = cust_agg["total_quantity"] / cust_agg["frequency"]

    # --- Step 4: Scaling + Clustering ---
    features = ["recency_days", "frequency", "monetary", "avg_basket", "distinct_products"]
    X = cust_agg[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    cust_agg["kmeans_cluster"] = kmeans.fit_predict(X_scaled)

    # --- Step 5: PCA for visualization ---
    pca = PCA(n_components=2, random_state=42)
    pca_proj = pca.fit_transform(X_scaled)
    cust_agg["pc1"] = pca_proj[:, 0]
    cust_agg["pc2"] = pca_proj[:, 1]

    # --- Step 6: Save processed dataset ---
    cust_agg.to_csv(PROCESSED_DATA_PATH, index=False)

    return cust_agg

# =========================
# Streamlit App
# =========================
st.set_page_config(layout="wide", page_title="Customer Segmentation Dashboard")
st.title("Customer Segmentation Dashboard")

# Load data (generate if not present)
if os.path.exists(PROCESSED_DATA_PATH):
    cust = pd.read_csv(PROCESSED_DATA_PATH)
else:
    st.info("Processed file not found. Running preprocessing pipeline...")
    cust = preprocess_and_cluster()

st.sidebar.header("Filters")
cluster_options = sorted(cust["kmeans_cluster"].unique())
selected_cluster = st.sidebar.selectbox("Select cluster", options=["All"] + list(cluster_options))

if selected_cluster == "All":
    subset = cust.copy()
else:
    subset = cust[cust["kmeans_cluster"] == int(selected_cluster)].copy()

st.header("Cluster summary")
st.write("Customers in view:", len(subset))
st.dataframe(subset.describe())

col1, col2 = st.columns(2)
with col1:
    st.subheader("Monetary distribution")
    fig1 = px.histogram(subset, x="monetary", nbins=50, title="Monetary")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.subheader("Recency distribution")
    fig2 = px.histogram(subset, x="recency_days", nbins=50, title="Recency (days)")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("2D PCA scatter (interactive)")
fig3 = px.scatter(subset, x="pc1", y="pc2", color="kmeans_cluster",
                  hover_data=["Customer ID", "monetary"])
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("Top customers by monetary value")
st.dataframe(subset.sort_values("monetary", ascending=False).head(20))
