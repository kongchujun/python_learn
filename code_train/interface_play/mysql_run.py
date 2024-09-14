from code_train.interface_play.mysql_database import MySQLConnector
# Initialize the MySQL connector
db = MySQLConnector(
    host='localhost',
    port=3306,
    database='mydb',
    user='myuser',
    password='mypassword'
)

# Create a table
db.create_table('users', {
    'id': 'INT AUTO_INCREMENT PRIMARY KEY',
    'name': 'VARCHAR(100)',
    'email': 'VARCHAR(100)'
})

# Insert data
db.insert('users', {'name': 'John Doe', 'email': 'john@example.com'})

# Query data
users = db.query('users')
print(users)

# Delete data
db.delete('users', "name='John Doe'")

# Close the connection
db.close()
