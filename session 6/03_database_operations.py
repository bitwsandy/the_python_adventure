# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Host where the database server is located
            user='root',    # Username used to log in to the database
            password='root',# Password used to log in to the database
            database='tg117' # Database to connect to
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    """Execute a single query such as CREATE, INSERT, UPDATE, DELETE"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    """Execute a query to read data from the database"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Establishing the database connection
connection = create_connection()

# Creating a new table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT, 
    name VARCHAR(255) NOT NULL, 
    age INT, 
    PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_table_query)

# Inserting records into the table
insert_query = """
INSERT INTO users (name, age) VALUES ('Alice', 24), ('Bob', 19)
"""
execute_query(connection, insert_query)

# Reading data from the table
select_query = "SELECT * FROM users"
users = execute_read_query(connection, select_query)
for user in users:
    print(user)

# Updating a record in the table
update_query = "UPDATE users SET age = 20 WHERE name = 'Bob'"
execute_query(connection, update_query)

# Deleting a record from the table
delete_query = "DELETE FROM users WHERE name = 'Alice'"
execute_query(connection, delete_query)

# Demonstrating transaction management
try:
    connection.start_transaction()
    # Example transaction: update and delete
    execute_query(connection, "UPDATE users SET age = 22 WHERE name = 'Bob'")
    execute_query(connection, "DELETE FROM users WHERE name = 'Alice'")
    connection.commit() # Commit changes
    print("Transaction is successful")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    connection.rollback() # Roll back changes on error
    print("Transaction failed and rolled back")

# Closing the connection
connection.close()
