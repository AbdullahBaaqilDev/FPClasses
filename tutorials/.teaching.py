import pypyodbc

# Define the connection string
conn_str = 'Driver={SQL Server};Server=ABDULLAH-LAPTOP\\SQLExpress;Trusted_Connection=yes;'

# Establish a connection to the SQL Server with autocommit mode
connection = pypyodbc.connect(conn_str, autocommit=True)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the SQL query to create the database
create_db_query = 'CREATE DATABASE your_database_name;'

# Execute the create database query
cursor.execute(create_db_query)

# Close the cursor and the database connection
cursor.close()
connection.close()