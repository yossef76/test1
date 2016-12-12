import sqlite3

con = sqlite3.connect("ramilevi.db3")

con.execute("""
  CREATE TABLE IF NOT EXISTS motzarim (
    id INTEGER PRIMARY KEY,
    barcode INTEGER,
    name CHAR,
    price REAL
  )
""")
con.execute("""
  CREATE TABLE IF NOT EXISTS mivtzaim (
    id INTEGER PRIMARY KEY,
    motzar_id INTEGER REFERENCES motzarim,
    start INTEGER,
    end INTEGER,
    price REAL
  )
""")

con.execute("""
  INSERT INTO motzarim(barcode,name,price) VALUES (?,?,?)
""", (222,'bread',3.5))
con.commit()