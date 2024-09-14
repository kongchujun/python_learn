import psycopg2
from psycopg2 import sql
from code_train.interface_play.database import DatabaseConnector
# Concrete subclass for PostgreSQL
class PostgresConnector(DatabaseConnector):
    def __init__(self, host, port, database, user, password):
        """
        Initialize the PostgreSQL connection.

        :param host: Database host.
        :param port: Database port.
        :param database: Database name.
        :param user: Username.
        :param password: Password.
        """
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Create a table in PostgreSQL.

        :param table_name: Name of the table to create.
        :param columns: Dictionary of column names and data types.
        """
        columns_definitions = ', '.join(f"{col} {dtype}" for col, dtype in columns.items())
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions});"
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def query(self, table_name, columns='*', conditions=None):
        """
        Query data from PostgreSQL.

        :param table_name: Name of the table to query.
        :param columns: Columns to select (list or '*').
        :param conditions: Conditions for the query.
        :return: Query results.
        """
        if isinstance(columns, list):
            columns_str = ', '.join(columns)
        else:
            columns_str = columns
        query_sql = f"SELECT {columns_str} FROM {table_name}"
        if conditions:
            query_sql += f" WHERE {conditions}"
        self.cursor.execute(query_sql)
        return self.cursor.fetchall()

    def insert(self, table_name, data):
        """
        Insert data into PostgreSQL.

        :param table_name: Name of the table to insert data into.
        :param data: Dictionary of data to insert.
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_sql, list(data.values()))
        self.conn.commit()

    def delete(self, table_name, conditions):
        """
        Delete data from PostgreSQL.

        :param table_name: Name of the table to delete data from.
        :param conditions: Conditions for deletion.
        """
        delete_sql = f"DELETE FROM {table_name} WHERE {conditions}"
        self.cursor.execute(delete_sql)
        self.conn.commit()

    def close(self):
        """Close the PostgreSQL connection."""
        self.cursor.close()
        self.conn.close()
