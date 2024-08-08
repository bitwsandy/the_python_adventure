# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

class DBContextManager:
    """Context manager for MySQL database connections."""
    def __init__(self, host, user, password, database):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """Ensure the connection is closed."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection is closed.")

def write_data_to_file(filename, data):
    """Write data to a file using a context manager."""
    with open(filename, 'w') as file:
        for row in data:
            file.write(f"{row}\n")
        print("Data written to file successfully.")

def main():
    # Database credentials (replace with your own)
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'tg117'

    # SQL Query
    query = "SELECT * FROM your_table"  # Update this to your specific SQL query

    # File to write to
    filename = "output.txt"

    # Using the DBContextManager to handle the database connection
    with DBContextManager(host, user, password, database) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

    # Writing data to file
    write_data_to_file(filename, results)

if __name__ == "__main__":
    main()

