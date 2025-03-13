import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="nida",  # New user
        password="2822016abc@",  # Your password
        database="library_db",  # Replace with your actual database name
        auth_plugin="caching_sha2_password"  # Explicitly use caching_sha2_password
    )
