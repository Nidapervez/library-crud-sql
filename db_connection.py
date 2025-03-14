import mysql.connector
import streamlit as st

def get_connection():
    secrets = st.secrets["mysql"]  # Fetch secrets from Streamlit

    return mysql.connector.connect(
        host=secrets["host"],
        user=secrets["user"],
        password=secrets["password"],
        database=secrets["database"],
        auth_plugin=secrets["auth_plugin"]
    )
