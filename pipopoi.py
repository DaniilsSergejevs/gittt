import sqlite3
conn = sqlite3.connect('etobaza1.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   ID INT PRIMARY KEY,
   Prod TEXT,
   Zīm TEXT,
   Teh TEXT,
   Cena NUMERIC);
""")
conn.commit()
more_users = [('00001', 'Cirvis', 'Bosch', 'liels', '30'), ('00002', 'Nazis', 'Bosch', 'ass', '50'), ('00003', 'Rulete', 'Fisko', '50m', '50'), ('00004', 'Skrūv.', 'DeWalt', 'neass', '3'), ('00005', 'Āmurs', 'Bosch', 'smags', '10'),]
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?, ?);", more_users)
conn.commit()