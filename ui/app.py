import streamlit as st
import requests

st.title("Semantic Search vs Keyword Search")

query = st.text_input("Enter your search query")

if st.button("Search"):

    keyword = requests.get(
        f"http://localhost:8000/api/search/keyword?q={query}"
    ).json()

    semantic = requests.get(
        f"http://localhost:8000/api/search/semantic?q={query}"
    ).json()

    col1, col2 = st.columns(2)

    with col1:
        st.header("Keyword Search")

        for r in keyword:
            st.subheader(r["title"])
            st.write(r["content"])

    with col2:
        st.header("Semantic Search")

        for r in semantic:
            st.subheader(r["title"])
            st.write(r["content"])
            st.write("Similarity:", r["score"])