##Archivo encargado de manejar la relación con la BD (Sin APIs)
from Section_06_Context_Manager.database_connection import DatabaseConnection

SERVER = 'MY_SERVER'
DB = 'MY_BD'


def insert_user(user):
    with DatabaseConnection(server=SERVER, database=DB) as connection:
        # Aquí va el llamado de insert a la BD
        pass

