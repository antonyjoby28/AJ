import streamlit as st
import pickle

st.set_page_config(
    page_title="CineVerse",
    page_icon="🎬"
)

st.markdown("""
<style>
.stApp {
    background-color: #1E1E2F;
}
</style>
""", unsafe_allow_html=True)

st.title("Movie Recommender App")
st.write("App is running successfully 🚀")

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='color:gold; text-align:center;'>🎬 THE CINEVERSE</h1>",
    unsafe_allow_html=True
)


movie_list['title'].tolist()

selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button("Recommend"):
    for movie in recommend(selected_movie):
        st.write(movie)
        
