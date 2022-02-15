import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
      conn = sqlite3.connect('Sales.db')
      return conn
    except Error:
      print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)

    print("\nDelete saleman of ID 5003:")
    s_id=5003
    cursorObj.execute(""" 
    DELETE FROM saleman
    WHERE saleman_id=?
    """;(s_id))
    conn.commit()
    cursorObj.execute("SELECT * FROM saleman")
    rows=cursorObj.fetchall()

sqllite_conn  = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
