# 🚓 PatrolIQ – Smart Safety Analytics Platform

## 📌 Overview
**PatrolIQ** is an end-to-end **Urban Safety & Crime Analytics platform** that uses **unsupervised machine learning** to analyze large-scale crime data and identify **crime hotspots, temporal patterns, and high-risk zones**.

Built using **500,000 Chicago crime records**, the platform helps law enforcement agencies make **data-driven patrol and resource allocation decisions** through interactive **Streamlit dashboards** and **MLflow-tracked models**.

---

## 🎯 Objective
- Identify geographic crime hotspots using clustering
- Discover high-risk time patterns (hour/day/season)
- Simplify complex crime data using dimensionality reduction
- Track experiments using **MLflow**
- Deploy a **production-ready Streamlit Cloud application**

---

## 🧰 Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **K-Means, DBSCAN, Hierarchical Clustering**
- **PCA, t-SNE / UMAP**
- **MLflow (Experiment Tracking)**
- **Streamlit (Cloud Deployment)**
- **Geographic & Temporal Data Analysis**

---

## 📊 Dataset
- **Source:** Chicago Police Department (Public Dataset)
- **Total Records:** 7.8 Million (Sample Used: 500,000)
- **Crime Types:** 33 categories
- **Features:** 22 crime, geographic & temporal variables
- **Coverage:** Chicago districts, beats, wards

---

## 🔧 Key Project Components

### 🧹 Data Processing
- Sampling & preprocessing of large dataset
- Missing value & inconsistency handling
- Temporal feature extraction (hour, day, month, season)

### ⚙️ Feature Engineering
- Time-based features (weekend, season)
- Geographic normalization (lat/long)
- Crime severity scoring
- Categorical encoding

### 🤖 Unsupervised Learning
**Clustering Algorithms (≥3):**
- K-Means
- DBSCAN
- Hierarchical Clustering  

**Temporal Clustering:**
- Identify peak crime hours & seasons

### 📉 Dimensionality Reduction
- **PCA** for variance explanation (70%+)
- **t-SNE / UMAP** for 2D visualization
- Feature importance identification

---

## 🔍 MLflow Integration
- Track clustering parameters & metrics
- Log PCA variance & model artifacts
- Compare algorithms using silhouette score
- Model versioning via MLflow registry

---

## 🌐 Streamlit Application
- Multi-page interactive dashboard
- Crime hotspot maps & heatmaps
- Temporal crime analysis
- Dimensionality reduction visualizations
- MLflow experiment monitoring

---

## 🚀 Outcomes
- Identified **5–10 high-risk crime zones**
- Discovered **peak crime time windows**
- Simplified 22+ features into 2–3 key dimensions
- Enabled **data-driven police patrol planning**
- Scalable **public safety analytics platform**

---


---

## 👤 Author
**Vishal Singla**

**Verified By:** Subhash Govindharaj  
**Approved By:** Nehlath Harmain  

⭐ Star the repository if you find it useful!



