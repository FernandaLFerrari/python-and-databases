import mysql.connector

class conexao:
    def __init__(self, host, dbname, user, password) -> None:
        self.host = host
        self.user = user
        self.database= dbname
        self.password = password
        
        global conn
        conn = mysql.connector.connect(host=self.host, database=self.database,
                                       user= self.user, password=self.password)
        
        try:
            if (conn.is_connected):
                print("Conectado ao banco de dados")
        except:
            print("Erro de conexão")
            
    def listaProdutos(self):
        cursor = conn.cursor()
        cursor.execute('SELECT nome_produto FROM produtos;')  
        linhas = cursor.fetchall()
        print('Total de registros:' + str(cursor.rowcount))
        for linha in linhas:
            print(str(linha[0]) + '-' + linha[1])  
            
    def insereProdutos(self, value):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome_produto) VALUES ('" + value + "');')
        conn.commit()
        print('Produto cadastrado!')
        
    def excluiProduto(self, id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id_produto = ' + str(id) + ';')
        conn.commit()
        print('Produto excluido!')
        
    
conexao_db = conexao('localhost', 'loja', 'root', '')
conexao.listaProdutos()