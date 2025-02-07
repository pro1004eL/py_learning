import pathlib
import sqlite3
import os

current_dir = pathlib.Path().absolute()
base_dir = pathlib.Path(current_dir).parent.parent


def test_connect_to_sqlite():
    conn = sqlite3.connect(os.path.join(base_dir, 'sqlite3_file_db.db'))
    cursor = conn.cursor()

#     cursor.execute("""CREATE TABLE products (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 	name TEXT NOT NULL,
# 	description TEXT,
# 	price INTEGER
# );
# """)
#
#
#     cursor.execute("""CREATE TABLE categories (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 	name INTEGER,
# 	CONSTRAINT categories_products_FK FOREIGN KEY (id) REFERENCES products(id)
# );""")
#
#     CREATE
#     TEMPORARY
#     TABLE
#     temp
#     AS
#     SELECT
#     id,
#     name,
#     description,
#     price,
#     category_id
#
#
# FROM
# products;

    #DROP TABLE products;

    cursor.execute("""
    
CREATE TABLE products (
	id INTEGER NOT NULL,
	category_id NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	price INTEGER
);


""")



    conn.commit()




