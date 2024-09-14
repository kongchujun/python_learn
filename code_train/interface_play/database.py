from abc import ABC, abstractmethod

# Abstract base class for database connection
class DatabaseConnector(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def create_table(self, table_name, columns):
        """
        Create a table in the database.

        :param table_name: Name of the table to create.
        :param columns: Dictionary of column names and data types.
        """
        pass

    @abstractmethod
    def query(self, table_name, columns='*', conditions=None):
        """
        Query data from the database.

        :param table_name: Name of the table to query.
        :param columns: Columns to select.
        :param conditions: Conditions for the query.
        :return: Query results.
        """
        pass

    @abstractmethod
    def insert(self, table_name, data):
        """
        Insert data into the database.

        :param table_name: Name of the table to insert data into.
        :param data: Dictionary of data to insert.
        """
        pass

    @abstractmethod
    def delete(self, table_name, conditions):
        """
        Delete data from the database.

        :param table_name: Name of the table to delete data from.
        :param conditions: Conditions for deletion.
        """
        pass

    @abstractmethod
    def close(self):
        """Close the database connection."""
        pass
