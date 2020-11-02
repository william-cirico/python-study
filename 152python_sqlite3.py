import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = "INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)"
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, pk):
        consulta = "UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?"
        self.cursor.execute(consulta, (nome, telefone, pk))
        self.conn.commit()

    def excluir(self, pk):
        consulta = "DELETE FROM agenda WHERE id=?"
        self.cursor.execute(consulta, (pk,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM agenda")

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, nome):
        consulta = "SELECT * FROM agenda WHERE nome LIKE ?"
        self.cursor.execute(consulta, (f"%{nome}%",))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    agenda = AgendaDB("agenda.db")
    agenda.inserir("William", "(47) 98408-8520")
    agenda.inserir("Maria", "(47) 98407-3520")
    agenda.listar()
    agenda.fechar()