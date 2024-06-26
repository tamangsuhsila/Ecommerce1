import sqlite3

# Step 2: Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Step 3: Create a cursor object
cur = conn.cursor()

# Step 4: Define the DELETE SQL statement
# This example deletes rows where the id is 1
delete_sql = 'DELETE FROM account_user'

# Step 5: Execute the DELETE statement
cur.execute(delete_sql)

# Step 6: Commit the changes
conn.commit()

# Step 7: Close the cursor and connection
cur.close()
conn.close()