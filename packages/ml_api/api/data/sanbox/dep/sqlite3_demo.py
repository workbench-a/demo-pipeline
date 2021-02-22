import sqlite3

connection = sqlite3.connect("test.db")

# print(connection.total_changes)

# cursor = connection.cursor()
# cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
# cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
# cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

# Read all
# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

connection.commit()

# # Read
# target_fish_name = "Jamie"
# rows = cursor.execute(
#     "SELECT name, species, tank_number FROM fish WHERE name = ?",
#     (target_fish_name,),
# ).fetchall()
# print(rows)

# # Update
# new_tank_number = 2
# moved_fish_name = "Sammy"
# cursor.execute(
#     "UPDATE fish SET tank_number = ? WHERE name = ?",
#     (new_tank_number, moved_fish_name)
# )

# # Confirm update
# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

# # Delete
# released_fish_name = "Sammy"
# cursor.execute(
#     "DELETE FROM fish WHERE name = ?",
#     (released_fish_name,)
# )

# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

# # In reality we need to cleanup (the connection) after ourselves
from contextlib import closing

with closing(sqlite3.connect("aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
      # Do all or any of the above CRUD operations here
        cursor.execute("INSERT INTO fish VALUES ('Jamie2', 'cuttlefish2', 72)")
        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)
    # commit changes before closing connection
    connection.commit()