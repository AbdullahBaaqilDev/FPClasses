import pypyodbc

DRIVER_NAME = "SQL Server"
SERVER_NAME = "ABDULLAH-LAPTOP\\SQLExpress"
DATABASE_NAME = "test1"

try:
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
    """

    connection = pypyodbc.connect(connection_string, autocommit=True)
    db = connection.cursor()

    # query = "CREATE TABLE cars (name VARCHAR(50) PRIMARY KEY, color VARCHAR(15), price DECIMAL(10, 2))"
    # db.execute(query)
except Exception as error:
    print("Couldn't connect to database")
    print(error)
finally:
    db.close()
    connection.close()

# -------------Create a Database
# db.execute("CREATE DATABASE test1")

# -------------Create a Table
    # query = "CREATE TABLE cars (name VARCHAR(50) PRIMARY KEY, color VARCHAR(15), price DECIMAL(10, 2))"
    # db.execute(query)

# -------------Delete a Table
    # db.execute("DROP TABLE cars")

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
    
# ------------Get the data from the database
# query = "SELECT * FROM cars"
# db.execute(query)
# print(db.fetchall())