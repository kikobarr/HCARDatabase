import mariadb

# Connect to MariaDB
try:
    dataBase = mariadb.connect(
        host="localhost",
        user="root",
        password="password1"
    )

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database
    cursorObject.execute("CREATE DATABASE kikodb")

    print("All done!")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    if 'dataBase' in locals() and dataBase:
        dataBase.close()  # Close the connection
