
import streamlit as st
import pickle
import numpy as np

movie_list= pickle.load(open('movie_list.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))
new= pickle.load(open('new.pkl','rb'))

st.title("Movie Recommonder")
movie= st.selectbox('movie',movie_list)
if st.button('RECOMMEND'):
    def recommend(movie):
        index = new[new['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distances[1:6]:
            st.subheader(new.iloc[i[0]].title)

    recommend(movie)

