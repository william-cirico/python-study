import sqlite3

conexao = sqlite3.connect("basedados.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "nome TEXT,"
               "peso REAL"
               ")")

cursor.execute("INSERT INTO clientes (nome, peso) VALUES (?, ?)", ("João", 50))
cursor.execute("INSERT INTO clientes VALUES (:id, :nome, :peso)", {"id": None, "nome": "Maria", "peso": 60})
cursor.execute("INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)", {"nome": "Edinei", "peso": 70})
conexao.commit()

cursor.execute("UPDATE clientes SET nome=:nome WHERE id=:id", {"nome": "Joana", "id": 3})

cursor.execute("DELETE FROM clientes WHERE id=:id", {"id": 2})

cursor.execute("SELECT * FROM clientes")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
