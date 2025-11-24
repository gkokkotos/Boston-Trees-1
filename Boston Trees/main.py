"""
Name: Grace Kokkotos
Date: 2025-11-23
Description: Main file controlling page navigation
"""

# Imports
import streamlit as st
from table_page import table_page
from map_page import map_page
from bar_chart_page import bar_chart_page
from scatter_page import scatter_page

# Set up page title and layout (only once)
st.set_page_config(
    page_title="Boston Trees Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar page selector
page = st.sidebar.selectbox("Select Page", ["Home", "Interactive Table", "Map of Trees", "Top 30 Trees Chart", "Diameter by Neighborhood"])

# Page logic
if page == "Home":
    st.title("Welcome to Boston Trees Explorer")
    st.write(
        "This interactive dashboard shows Boston street & park trees.\n"
        "Use the sidebar to navigate to different pages."
    )
# call the function from table_page.py
elif page == "Interactive Table":
    table_page()
# call the function from map_page.py
elif page == "Map of Trees":
    map_page()
elif page == "Top 30 Trees Chart":
    bar_chart_page()
elif page == "Diameter by Neighborhood":
    scatter_page()
