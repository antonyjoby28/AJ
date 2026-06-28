import streamlit as st
import pickle

st.set_page_config(
    page_title="CineVerse",
    page_icon="🎬"
)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

st.title("Movie Recommender App")
st.write("App is running successfully 🚀")

st.markdown(
    "<h1 style='color:gold; text-align:center;'>🎬 THE CINEVERSE</h1>",
    unsafe_allow_html=True
)

# ==========================================
# 1. LOAD YOUR PICKLE DATA HERE BEFORE USING IT
# ==========================================
# Replace 'movies_dict.pkl' with your actual movie file name if it's different
movies_import = pickle.load(open('movies.pkl', 'rb')) 
# Replace 'similarity.pkl' with your actual similarity file name
similarity = pickle.load(open('similarity.pkl', 'rb'))

# If your pickle file was saved as a dictionary, convert it back to a DataFrame:
import pandas as pd
movies = pd.DataFrame(movies_import)

# Now extract the titles into movie_list safely
movie_list = movies['title'].tolist()
# ==========================================

# 2. PASS THE LIST OF TITLES TO THE SELECTBOX
selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    # Fixed variable name conflict here to avoid overriding internal names
    matched_movies = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in matched_movies:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button("Recommend"):
    for movie in recommend(selected_movie):
        st.write(movie)