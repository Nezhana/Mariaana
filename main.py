# main file
import streamlit as st
st.title('Мар'янка')

volume = st.slider('Для того, щоб змінити швидкість, надайте значення від нуля до ста.', 0, 100, 100)
rate = st.slider('Для того, щоб змінити гучність, надайте значення від нуля до ста.', 0, 100, 100)

st.write(volume, rate)
