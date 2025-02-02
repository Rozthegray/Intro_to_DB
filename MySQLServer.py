import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Computer77"
    )

    cursor = connection.cursor()
    
    # Create database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
