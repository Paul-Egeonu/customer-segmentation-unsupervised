
![stock-photo-customer-segmentation-models-concept-segments-with-colorful-cubes-2220539983](https://github.com/user-attachments/assets/a87dc82f-a47b-4cfe-89bf-5c5b3348db93)


# 🧑‍🤝‍🧑 Customer Segmentation with Unsupervised Learning  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Scikit-Learn](https://img.shields.io/badge/ML-ScikitLearn-orange)  
![Tableau](https://img.shields.io/badge/Tableau-Visualization-blue?logo=tableau&logoColor=white)  
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)  

This project applies **unsupervised machine learning** to segment customers into distinct groups based on behavioral and transactional data.  
The insights help businesses tailor marketing strategies, improve retention, and personalize customer engagement.  

---

## 📂 Project Structure  

```
customer_segmentation_full_project/
│── data/
│   └── online_retail_II.csv               # Raw transactional dataset
│── customer_aggregates.csv                # Aggregated customer features (frequency, recency, monetary)
│── customer_aggregates_with_clusters.csv  # Final dataset with cluster assignments
│── kmeans_cluster_profile.csv             # Cluster profile summary
│── Customer_Segmentation.ipynb            # Original analysis notebook
│── Customer_Segmentation_portfolio.ipynb  # Enhanced notebook with markdown explanations
│── scaler_customer_seg.pkl                # Preprocessing scaler
│── kmeans_customer_seg.pkl                # Saved KMeans model
│── Customer_Segmentation.twb              # Tableau workbook (visualizations)
│── segmentation_app.py                    # Python script for predictions
│── README.md                              # Project documentation
│── requirements.txt                       # Dependencies
```

---

## 📊 Dataset  

- **Raw File:** `online_retail_II.csv` (in the `data/` folder)  
- **Description:** Transactional data from an online retail store, including invoice, stock code, description, quantity, price, customer ID, and country.  
- **Goal:** Transform raw transactions into aggregated customer-level features for clustering.  

**Processed Outputs:**  
- `customer_aggregates.csv` → Aggregated features per customer (recency, frequency, monetary value, etc.)  
- `customer_aggregates_with_clusters.csv` → Includes assigned cluster labels  
- `kmeans_cluster_profile.csv` → Summary statistics for each cluster  

---

## 🔎 Workflow  

1. **Data Preparation & Exploration**  
   - Load raw transactional data (`online_retail_II.csv`)  
   - Aggregate into customer-level features (RFM metrics)  
   - Handle missing values and outliers  
   - Scale numerical features for clustering  

2. **Clustering (KMeans)**  
   - Applied **KMeans algorithm**  
   - Determined optimal number of clusters using **Elbow method** and **Silhouette score**  
   - Saved preprocessing pipeline (`scaler_customer_seg.pkl`) and trained model (`kmeans_customer_seg.pkl`)  

3. **Cluster Profiling**  
   Descriptive business labels for clusters:  
   - **Cluster 0:** Price-sensitive, low spenders  
   - **Cluster 1:** Loyal, high-value customers  
   - **Cluster 2:** Occasional, moderate engagement  
   - **Cluster 3:** High-frequency, promotion-driven customers  

   📄 See `kmeans_cluster_profile.csv` for detailed stats.  

4. **Visualization (Tableau)**  
   Interactive dashboard (`Customer_Segmentation.twb`) with:  
   - Cluster size distribution  
   - Feature averages per cluster  
   - 2D cluster projections  

   👉 **[Insert Tableau dashboard screenshots here]**  

5. **Deployment**  
   - `segmentation_app.py`: Python script to predict cluster membership for new customers  
   - Can be extended into a **Streamlit app** for interactive use  

 **STREAMLIT DASHBOARD** 
 
![CustomerSegmentationDashboard-Personal-MicrosoftEdge2025-10-0312-14-37-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/fda44970-990d-4296-9e77-5ca786bb2728)

---

## 📈 Key Insights  

- Raw retail transactions can be aggregated into **RFM-style features** for segmentation.  
- Customers can be grouped into **4 meaningful clusters** with distinct behavioral patterns.  
- Results provide actionable insights for:  
  - Targeted marketing campaigns  
  - Loyalty rewards programs  
  - Retention strategies  

---

## 🚀 How to Run  

### 1. Clone repository  
```bash
git clone https://github.com/yourusername/customer-segmentation-unsupervised.git
cd customer-segmentation-unsupervised
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Run Notebook  
```bash
jupyter notebook Customer_Segmentation_portfolio.ipynb
```

### 4. Run Prediction Script  
```bash
streamlit ru segmentation_app.py
```

### 5. Open Tableau Dashboard  
Load `Customer_Segmentation.twb` in Tableau Desktop or Tableau Public.  

---

## 📌 Future Improvements  

- Try **Hierarchical Clustering** and **DBSCAN**  
- Automate pipeline for live/streaming data  
- Build full **Streamlit + Tableau embedded dashboard**  

---

## 🏆 Author  

**Paul Egeonu**  
_Data Analyst | Data Scientist_  
[LinkedIn](https://www.linkedin.com/in/paul-egeonu) | [GitHub](https://github.com/Paul-Egeonu) 
