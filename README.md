# 🎬 Movie Recommender System

A **content-based movie recommender system** built using **Python** and **Streamlit** that suggests top 5 similar movies based on user selection. The recommendations are based on **cosine similarity** scores calculated from movie features.

---

## 🚀 Demo

[Movie Recommender System - Live Demo](https://shubhamdobariya-movie-recommender-system-app-ogly9n.streamlit.app/)

---

## 📌 Features

- Recommends top 5 similar movies based on selected movie
- Fetches movie posters using **TMDB API**
- Deployed using **Streamlit**
- Managed large model file (`similarity.pkl`) via **Google Drive**
- Clean and responsive UI using Streamlit components

---

## 🧠 Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- TMDB API
- Google Drive (for large model file hosting)

---

## 🚀 Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ShubhamDobariya/Olympics-Data-Analysis.git
   cd Movie-Recommender-System

2. **Install dependencies:**:

   ```bash
   pip install -r requirements.txt

3. **Download `similarity.pkl` from Google Drive:

   [Download the file using this link](https://drive.google.com/file/d/1lI64w0WwHN2SWI5kNrmufp_Ys_qpzaZs/view?usp=sharing)

   
4. **Run the application:

   ```bash
   streamlit run app.py
