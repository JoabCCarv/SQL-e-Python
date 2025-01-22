import sqlite3 as sql

class TransactionObject:
    def __init__(self, database='clientes.db'):
        """Inicializa a conexão com o banco de dados"""
        self.database = database
        self.conn = None
        self.cur = None
        self.connected = False

    def connect(self):
        """Conecta ao banco de dados"""
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self.connected:
            self.conn.close()
            self.connected = False

    def execute(self, query, parms=None):
        """Executa uma query no banco de dados"""
        if self.connected:
            if parms is None:
                self.cur.execute(query)
            else:
                self.cur.execute(query, parms)
            return True
        else:
            return False

    def fetchall(self):
        """Retorna todos os resultados da última query"""
        return self.cur.fetchall()

    def persist(self):
        """Grava as mudanças no banco de dados"""
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False


# Funções de manipulação do banco de dados
def initDB():
    """Inicializa o banco de dados e cria a tabela, se necessário"""
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)"
    )
    trans.persist()
    trans.disconnect()


def insert(nome, sobrenome, email, cpf):
    """Insere um novo cliente no banco de dados"""
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf)
    )
    trans.persist()
    trans.disconnect()


def view():
    """Retorna todos os registros do banco de dados"""
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM cliente")
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def search(nome="", sobrenome="", email="", cpf=""):
    """Busca registros no banco de dados com base nos critérios fornecidos"""
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "SELECT * FROM cliente WHERE nome=? OR sobrenome=? OR email=? OR cpf=?",
        (nome, sobrenome, email, cpf),
    )
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    """Deleta um registro do banco de dados com base no ID"""
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM cliente WHERE id=?", (id,))
    trans.persist()
    trans.disconnect()


def update(id, nome, sobrenome, email, cpf):
    """Atualiza um registro existente no banco de dados"""
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "UPDATE cliente SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?",
        (nome, sobrenome, email, cpf, id),
    )
    trans.persist()
    trans.disconnect()


# Inicializa o banco de dados ao executar o script
if __name__ == "__main__":
    initDB()