# 🎵 Music Recommendation System

This project is a **content-based music recommender system** built using **machine learning** and **audio feature clustering**. It helps users discover songs with similar musical characteristics (e.g., tempo, energy, danceability) using data from **Spotify**.
<img width="801" height="576" alt="image" src="https://github.com/user-attachments/assets/01d549ca-7af2-4cf2-a22d-f361ad3c0283" />

---

## 🔍 Problem Statement
With the rise of digital music platforms, users face difficulty in discovering songs aligned with their preferences, especially without sufficient listening history. Traditional collaborative filtering methods fail for new or broad-taste users. This system solves that with audio feature-based clustering and similarity.

---

## 🚀 Features
- 📊 Clustering songs using KMeans
- 🔁 Cosine similarity-based recommendation
- 🎧 Spotify audio features (danceability, tempo, etc.)
- 🧠 PCA & t-SNE visualizations
- 🌐 Interactive Streamlit app
- 🔍 Real-time recommendations

---

## 🧰 Technologies Used
- Python
- Pandas, NumPy
- scikit-learn
- Plotly, Matplotlib
- Spotipy (Spotify API)
- Streamlit

---

## 🧠 How It Works
1. Load `data.csv` from Kaggle or Spotify.
2. Preprocess and scale audio features.
3. Cluster songs using KMeans.
4. Recommend songs based on cosine similarity.
5. Access the recommendation engine via a Streamlit web app.

---
### Dataset
Download the dataset from [Kaggle](https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset)and place it in the project root folder as `data.csv`.

## ▶️ How to Run the App

```bash
git clone https://github.com/your-username/music-recommendation-system.git
cd music-recommendation-system
pip install -r requirements.txt
streamlit run streamlit_app.py
