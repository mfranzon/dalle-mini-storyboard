import streamlit as st
from dalle import create_and_show_images
from summary import summary_text
import io

st.title("DALL-E StoryBoard")

#text = st.text_input("What should I create?")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))

    text = stringio.read()

num_images = st.slider("How many images?", 1, 4)

ok = st.button("GO!")

if ok:
    chapters_summarized = summary_text(text)
    print(chapters_summarized)
    create_and_show_images(chapters_summarized, num_images)
