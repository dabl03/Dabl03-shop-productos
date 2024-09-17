from bcrypt import gensalt, hashpw;
#import mysql.connector; -- Cambiarlo por sqlite
import sqlite3

def gSqlite_connector():
	return sqlite3.connect("./database/productos.db");
def gdb_products(available:str)->str:
	"""Obtener los productos en formato json

	Parameters:
		available (str=('Si','No')): Indica si se quiere buscar los productos disponibles.
	""";
	db=gSqlite_connector();
	send_db=db.cursor();
	send_db.execute(f"SELECT * FROM Producto WHERE Available='{available}'");
	p=send_db.fetchall();
	db.close();
	return p;
