import streamlit as st
import pandas as pd
import time 
from datetime import datetime



ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=1000, limit=100)

if count == 0:
    st.write("")
elif count % 2 == 0 and count % 4 == 0:
    st.write("")
elif count % 3 == 0:
    st.write("")
elif count % 5 == 0:
    st.write("")
else:
    st.write("")

df = pd.read_csv("Attendance/Attendance_" + date + ".csv")


df['Date'] = date




df['Location'] = None

primary_color = "#3498db" 
secondary_color = "#2ecc71"  
background_color = "#f0f2f6" 
text_color = "#333333" 

st.markdown(
    f"""
    <style>
        .sidebar .sidebar-content {{
            background-color: {primary_color};
        }}
        .sidebar .sidebar-content .block-container {{
            color: #fff;
        }}
        .stButton > button {{
            background-color: {secondary_color} !important;
            color: #fff;
            border-radius: 4px;
            padding: 8px 12px;
            border: none;
            cursor: pointer;
        }}
        .stButton > button:hover {{
            background-color: {secondary_color} !important; /* Keep the same color on hover */
            color: #fff; /* Keep the same text color on hover */
        }}
        .st-c {{
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Location Tracker")
refresh_button = st.sidebar.button("Refresh Location")


st.title("Attendance Sheet")



st.sidebar.write("")
st.write("")


st.dataframe(df[['Date', 'Location'] + list(df.columns[:-2])].style.highlight_max(axis=0))