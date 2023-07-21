import streamlit as st
import pickle
import pandas as pd
import requests


def fatchposter(movie_id):
    reponse = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=61c019a332b0a4d2557da74c40b92359&language=en-US'.format(
            movie_id))
    data = reponse.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    re = []
    re_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        re.append(movies.iloc[i[0]].title)
        re_poster.append(fatchposter(movie_id))
    return re, re_poster


movie_dict = pickle.load(open('movies_dicti.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender system')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])
