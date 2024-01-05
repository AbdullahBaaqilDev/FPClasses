import mysql.connector

try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "--------------",
        database = "testdatabase1"
    )
    cursor = connection.cursor()
    delete_query = "DELETE FROM cars WHERE name = %s"
    name = "Toyota Camry"
    cursor.execute(delete_query, (name,))
    connection.commit()
except mysql.connector.Error:
    print("Could not connect to the database")


# -------Create a new table in database you must have connected to the database in connection section
# cursor.execute("CREATE TABLE cars (name VARCHAR(50), price DECIMAL(10, 2))")

# -------Add a column after making the table-------
# cursor.execute("ALTER TABLE cars ADD COLUMN color VARCHAR(10);")

# -------Insert a row to a table-------
# insert_query = "INSERT INTO cars (name, price, color) VALUES (%s, %s, %s)"
# values = ('Toyota Camry', 15000, 'red')
# cursor.execute(insert_query, values)# 1st para will ba the query and the 2ed the data if insterted and you have to format it is % way
# connection.commit()

# -------Update a row to a table-------
# update_query = "UPDATE cars SET price = %s WHERE name = %s"
# values = (88090, 'Toyota Corolla')
# cursor.execute(update_query, values)
# connection.commit()

# -------Delete row-------


# -------Delete column value in a row-------
# update_query = "UPDATE customers SET id = NULL WHERE id = %s"
# row_id = 1
# cursor.execute(update_query, (row_id,))
# connection.commit()

# -------Delete a Table-------
# delete_query = "DROP TABLE customers;"
# cursor.execute(update_query)
# connection.commit()