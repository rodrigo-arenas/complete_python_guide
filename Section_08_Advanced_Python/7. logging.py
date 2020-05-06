import logging

logging.basicConfig(level=logging.DEBUG,  # Hace visible desde el nivel DEBUG
                    format='%(asctime)s %(levelname)-8s:[%(filename)s:%(lineno)d] %(message)s',
                    datefmt='&d-%m-%Y %H:%M:%S',
                    filename='logs.txt')
logger = logging.getLogger(__name__)

"""
DEBUG -> No se muestra por defecto
INFO  -> No se muestra por defecto
WARNING
ERROR
CRITICAL

Otro patron común es tener:
logger = logging.getLogger(books)
haciendo referencia que es el main de una app books
logger = logging.getLogger(books.database)
haciendo referencia que se está en el modulo database, lo hereda


"""

logger.info('Info Message')
logger.warning("Warning Message")
