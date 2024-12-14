import streamlit as st
from app import app
if 'page' not in st.session_state:
    st.session_state.page = "homepage"

if st.session_state.page == "homepage":
    # exec(open("app.py").read())
    app()