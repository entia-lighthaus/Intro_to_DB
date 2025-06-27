#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (no database yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Lighthaus'  # 🔁 Replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
