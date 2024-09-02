import streamlit as st
from Introduction import *
from Portfolio import *
from Profile import *

st.set_page_config(
    page_title="My Profile",
    page_icon=":wave:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar
st.sidebar.title("Profile Navigation")
option = st.sidebar.radio(
    "",
    ("Introduction", "Portfolio", "Profile")
)

if option == "Introduction":
    introduction()
elif option == "Portfolio":
    portfolio()
elif option == "Profile":
    profile()
