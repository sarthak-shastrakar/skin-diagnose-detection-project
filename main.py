import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
load_dotenv()

import Homepage, consultant, chatbot, about, prediction

# Page Configuration
# st.set_page_config(page_title="DermaCare Hub", page_icon="🩺", layout="wide")

# Custom CSS for Sidebar Styling
st.markdown("""
    <style>
        /* Sidebar Background with Gradient */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #2c3e50, #4a69bd);
            color: white;
        }

        /* Sidebar Title Styling */
        .sidebar-title {
            font-size: 26px;
            font-weight: bold;
            color: #ffcc00;
            text-align: center;
            margin-bottom: 15px;
        }

        /* Option Menu Styling */
        .css-1v0mbdj a {
            font-size: 18px;
            font-weight: bold;
            color: white !important;
            text-decoration: none;
        }

        /* Hover & Active Effects */
        .css-1v0mbdj a:hover, .css-1v0mbdj .active {
            background: linear-gradient(to right, #ffcc00, #ff9900);
            color: black !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px;
        }
    </style>
""", unsafe_allow_html=True)

def load_bootstrap():
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    """, unsafe_allow_html=True)

# Multi-App Class
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run():
        # Sidebar with Option Menu
        with st.sidebar:
            st.markdown('<div class="sidebar-title">🩺 DermaCare Hub</div>', unsafe_allow_html=True)  
            app = option_menu(
                menu_title="Navigation",
                options=["🏠 Homepage", "📞 Consult a Doctor", "🤖 Chatbot", "📊 Prediction", "ℹ️ About"],
                icons=["house-fill", "person-circle", "chat-fill", "search-heart", "info-circle"],
                menu_icon="list",
                default_index=0,
                styles={
                    "container": {"padding": "7px", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "22px"},
                    "nav-link": {"color": "white", "font-size": "18px", "text-align": "left", "margin": "5px", "--hover-color": "#ffcc00"},
                    "nav-link-selected": {"background": "#ff9900", "color": "black", "font-weight": "bold"},
                }
            )

        # Page Content Based on Selection
        if app == "🏠 Homepage":
            Homepage.app()
        elif app == "📞 Consult a Doctor":
            consultant.app()
        elif app == "🤖 Chatbot":
            chatbot.app()
        elif app == "📊 Prediction":
            prediction.app()
        elif app == "ℹ️ About":
            about.app()

    run()


