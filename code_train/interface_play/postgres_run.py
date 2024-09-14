from code_train.interface_play.postgres_database import PostgresConnector

# Initialize the PostgreSQL connector
db = PostgresConnector(
    host='localhost',
    port=5432,
    database='postgres',
    user='postgres',
    password='postgres'
)

# Create a table
table_name = 'students'
db.create_table(table_name, {
    'id': 'SERIAL PRIMARY KEY',
    'name': 'VARCHAR(100)',
    'email': 'VARCHAR(100)'
})

# Insert data
db.insert(table_name, {'name': 'John Doe', 'email': 'john@example.com'})

# Query data
users = db.query(table_name)
print(users)

# Delete data
db.delete(table_name, "name='John Doe'")

# Close the connection
db.close()
