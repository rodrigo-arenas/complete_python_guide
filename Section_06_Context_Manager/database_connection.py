import pandas as pd
import pyodbc


class DatabaseConnection:
    """
    Creates a SQL Server connection using pyodbc
    """
    def __init__(self, server, database):
        self.connection = None
        self.server = server
        self.database = database

    def __enter__(self):
        self.connection = pyodbc.connect(Trusted_Connection='yes', driver='{SQL Server}',
                                         server=self.server, database=self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Se ejecuta al terminar de ejecutar el método
        #Si hay un error, se cierra la conexión a la DB sin enviar el query
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

