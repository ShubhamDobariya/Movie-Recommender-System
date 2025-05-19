import pickle
import streamlit as st
import requests
import os
import gdown

# page Configuration
st.set_page_config(layout="wide")

# Function to download similarity.pkl from Google Drive if it doesn't exist
def download_similarity_model():
    file_id = '1lI64w0WwHN2SWI5kNrmufp_Ys_qpzaZs'  # Your file ID
    url = f'https://drive.google.com/uc?id={file_id}'
    output_path = 'model/similarity.pkl'

    if not os.path.exists(output_path):
        st.info("Downloading similarity model from Google Drive...")
        os.makedirs('model', exist_ok=True)
        gdown.download(url, output_path, quiet=False)

# Download model if needed
download_similarity_model()

# Load models
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')


movie_list = movies['title'].values

cols = st.columns([4, 1])
with cols[0]:
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list,
        label_visibility="collapsed"
    )
with cols[1]:
    recommend_button = st.button('Show Recommendation')

if recommend_button:
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





