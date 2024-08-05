import streamlit as st
from snowflake.snowpark import Session
import snowflake.snowpark.functions as fn
import json 
import pandas as pd
import numpy as np
import spcs_helpers
import streamlit as st
from PIL import Image
import base64
import os
from pathlib import Path

# Set page config at the very beginning
st.set_page_config(page_title="Mobile App", layout="centered", initial_sidebar_state="collapsed")

# Get User from SPCS Headers
from streamlit.web.server.websocket_headers import _get_websocket_headers
user = _get_websocket_headers().get("Sf-Context-Current-User") or "Visitor"


# Set page config at the very beginning
#st.set_page_config(page_title="Mobile App", layout="wide", initial_sidebar_state="collapsed")

#Get User from SPCS Headers
from streamlit.web.server.websocket_headers import _get_websocket_headers
user = _get_websocket_headers().get("Sf-Context-Current-User") or "Visitor"


# Make connection to Snowflake and cache it
@st.cache_resource
def connect_to_snowflake():
    return spcs_helpers.session()

session = connect_to_snowflake()

#import streamlit as st

# Set page config
#st.set_page_config(page_title="Mobile App", layout="centered", initial_sidebar_state="collapsed")

import streamlit as st

# Set page config
#st.set_page_config(page_title="Mobile App", layout="centered", initial_sidebar_state="collapsed")


from streamlit.web.server.websocket_headers import _get_websocket_headers



# Get User from SPCS Headers
user = _get_websocket_headers().get("Sf-Context-Current-User") or "Visitor"


# Custom CSS to style the app and create a phone frame
st.markdown("""
<style>
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
    }
    .phone-container {
        width: 375px;
        height: 812px;
        background-color: white;
        border-radius: 50px;
        border: 16px solid black;
        overflow: hidden;
        position: relative;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    .phone-notch {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 200px;
        height: 30px;
        background-color: black;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
        z-index: 10;
    }
    .phone-content {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .top-bar {
        padding: 10px 20px;
        background-color: white;
        z-index: 5;
    }
    .main-content {
        flex-grow: 1;
        background-color: #e6f2ff;
        padding: 20px;
        display: flex;
        flex-direction: column;
    }
    .custom-button {
        background-color: transparent;
        color: #4CAF50;
        border: none;
        padding: 10px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 20px;
    }
    .search-container {
        position: relative;
        margin-top: 20px;
    }
    .search-input {
        width: 100%;
        padding: 15px 15px 15px 40px;
        border: 1px solid #ccc;
        border-radius: 25px;
        font-size: 16px;
    }
    .search-icon {
        position: absolute;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
    }
    .bottom-nav {
        display: flex;
        justify-content: space-around;
        padding: 15px;
        background-color: white;
    }
    .bottom-nav span {
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to change page
def change_page(page):
    st.session_state.page = page

# Home page content
def home_page():
    st.markdown(f"""
    <div class="phone-container">
        <div class="phone-notch"></div>
        <div class="phone-content">
            <div class="top-bar">
                <span>Search</span>
            </div>
            <div class="main-content">
                <h1 style="font-size: 24px; font-weight: bold; margin-bottom: 10px;">Hi Nima,</h1>
                <p style="font-size: 18px; margin-bottom: 20px;">Meeting with buyers or owners?</p>
                <div style="display: flex; justify-content: space-between; margin-bottom: 30px;">
                    <button class="custom-button" onclick="parent.postMessage({{type: 'streamlit:setComponentValue', value: 'buyers'}}, '*')">Buyers</button>
                    <button class="custom-button" onclick="parent.postMessage({{type: 'streamlit:setComponentValue', value: 'owners'}}, '*')">Owners</button>
                </div>
                <div class="search-container">
                    <span class="search-icon">🔍</span>
                    <input type="text" placeholder="try email address" class="search-input">
                </div>
            </div>
            <div class="bottom-nav">
                <span style="color: #FF69B4;">Search</span>
                <span>Saved</span>
                <span>Filter</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Buyers page content
def buyers_page():
    st.markdown("""
    <div class="phone-container">
        <div class="phone-notch"></div>
        <div class="phone-content">
            <div class="top-bar">
                <span>Buyers</span>
                <div class="profile-pic"></div>
            </div>
            <div class="main-content">
                <h2>Buyers Activity</h2>
                <div class="activity-box">
                    <h3>Last 6 months activity</h3>
                    <p>12 enquiries made in the last 1 month</p>
                </div>
                <div class="house-image">
                    House Image Placeholder
                </div>
                <button class="custom-button" style="margin-top: 20px;" onclick="parent.postMessage({type: 'streamlit:setComponentValue', value: 'home'}, '*')">Back to Home</button>
            </div>
            <div class="bottom-nav">
                <span style="color: #FF69B4;">Search</span>
                <span>Saved</span>
                <span>Filter</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Owners page content (placeholder)
def owners_page():
    st.markdown("""
    <div class="phone-container">
        <div class="phone-notch"></div>
        <div class="phone-content">
            <div class="top-bar">
                <span>Owners</span>
            </div>
            <div class="main-content">
                <h2>Owners Page</h2>
                <p>This is a placeholder for the Owners page content.</p>
                <button class="custom-button" style="margin-top: 20px;" onclick="parent.postMessage({type: 'streamlit:setComponentValue', value: 'home'}, '*')">Back to Home</button>
            </div>
            <div class="bottom-nav">
                <span style="color: #FF69B4;">Search</span>
                <span>Saved</span>
                <span>Filter</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main app logic
if 'widget_value' not in st.session_state:
    st.session_state.widget_value = None

# Hidden input to capture button clicks
widget_value = st.text_input("widget_value", key="widget_value", label_visibility="hidden")

# Check for button clicks and change page
if widget_value == 'buyers':
    change_page('buyers')
    st.session_state.widget_value = None
elif widget_value == 'owners':
    change_page('owners')
    st.session_state.widget_value = None
elif widget_value == 'home':
    change_page('home')
    st.session_state.widget_value = None

# Render the appropriate page
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'buyers':
    buyers_page()
elif st.session_state.page == 'owners':
    owners_page()

# Empty Streamlit elements to create space for our custom HTML
st.empty()
