
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
│── customer_aggregates.csv                # Raw aggregated customer data
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

- **File:** `customer_aggregates.csv`  
- **Description:** Aggregated customer behavioral and transactional features (frequency, monetary value, recency, etc.).  
- **Unsupervised Goal:** Segment customers into meaningful groups using clustering techniques.  

Processed outputs:  
- `customer_aggregates_with_clusters.csv` → includes assigned cluster labels  
- `kmeans_cluster_profile.csv` → cluster-wise summary statistics  

---

## 🔎 Workflow  

1. **Data Preparation & Exploration**  
   - Import data and explore feature distributions  
   - Handle missing values and outliers  
   - Scale numerical features for clustering  

2. **Clustering (KMeans)**  
   - Applied **KMeans algorithm**  
   - Determined number of clusters via **Elbow method** and **Silhouette score**  
   - Saved preprocessing pipeline (`scaler_customer_seg.pkl`) and trained model (`kmeans_customer_seg.pkl`)  

3. **Cluster Profiling**  
   Created descriptive labels for customer groups based on cluster centroids and behavioral metrics:  
   - **Cluster 0:** Price-sensitive, low spenders  
   - **Cluster 1:** Loyal, high-value customers  
   - **Cluster 2:** Occasional, moderate engagement  
   - **Cluster 3:** High-frequency, promotion-driven customers  

   📄 See `kmeans_cluster_profile.csv` for details.  

4. **Visualization (Tableau)**  
   Interactive dashboard built in Tableau (`Customer_Segmentation.twb`) with:  
   - Cluster size distribution  
   - Average feature values per cluster  
   - 2D cluster projection charts  

   👉 **[Insert Tableau dashboard screenshots here]**  

5. **Deployment**  
   - `segmentation_app.py`: Python script to predict cluster membership for new customers  
   - Can be extended into a **Streamlit app** for live customer segmentation  

   👉 **[Insert GIF of Streamlit app here]**  

---

## 📈 Key Insights  

- Customers can be meaningfully grouped into **4 clusters** with distinct behavioral patterns  
- High-value and promotion-driven segments present key opportunities for:  
  - Targeted marketing campaigns  
  - Loyalty programs  
  - Revenue maximization strategies  

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
python segmentation_app.py
```

### 5. Open Tableau Dashboard  
Load `Customer_Segmentation.twb` in Tableau Desktop or Tableau Public.  

---

## 📌 Future Improvements  

- Experiment with **Hierarchical Clustering** and **DBSCAN**  
- Automate cluster updates with streaming data  
- Deploy interactive segmentation dashboard (Streamlit + Tableau embedded)  

---

## 🏆 Author  

**Your Name**  
_Data Analyst & Data Scientist_  
[LinkedIn](https://www.linkedin.com/) | [Portfolio](https://yourportfolio.com) | [GitHub](https://github.com/yourusername)  
