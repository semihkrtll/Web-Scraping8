
import mysql.connector

def get_db_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",      
        database="cryptodb"
    )
    return db_connection
