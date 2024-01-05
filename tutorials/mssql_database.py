import pypyodbc

DRIVER_NAME = "SQL Server"
SERVER_NAME = "ABDULLAH-LAPTOP\\SQLExpress"


try:
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        Trusted_Connection=yes;
    """

    connection = pypyodbc.connect(connection_string, autocommit=True)
    db = connection.cursor()
    db.execute("CREATE DATABASE test2")
except Exception as error:
    print("Couldn't connect to database")
    print(error)
finally:
    db.close()
    connection.close()

# -------------Create a Table
    # query = "CREATE TABLE cars (name VARCHAR(50) PRIMARY KEY, color VARCHAR(15), price DECIMAL(10, 2))"
    # db.execute(query)

# ---------------add a rowٍ
# query = "INSERT INTO cars (name, price, color) VALUES (?, ?, ?)"
# values = ('Toyota Corolla', 127250.25, 'white')
# db.execute(query, values)
# connection.commit()

# ---------------update a row
# query = "UPDATE cars SET color = ?, price = ? WHERE name = ?"
# values = ("red", 127000.50, "Toyota Corolla")
# db.execute(query, values)
# connection.commit()

# ---------------delete a row
# query = "DELETE FROM cars WHERE name = ?"
# values = ('Toyota Corolla',)
# db.execute(query, values)
# connection.commit()

# -----------Delete a column from the table
# query = "ALTER TABLE cars DROP COLUMN color"
# db.execute(query)
# connection.commit()

# -----------Delete a table
# query = "DROP TABLE cars"
# db.execute(query)
# connection.commit()