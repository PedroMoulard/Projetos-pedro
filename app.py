import mysql.connector

conexao = mysql.connector.connect (
    host='localhost',
    user='root',
    password='Pen120219',
    database='crud_pedro',
)

cursor = conexao.cursor()

#CRUD

#CREATE

#nome_produto = "gabinete"
#valor = 600


#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
#cursor.execute(comando)
#conexao.commit()

#cursor.close()
#conexao.close()

#READ

# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()

# print(resultado)

# cursor.close()
# conexao.close()

#UPDATE

# nome_produto = "peça_pc"
# valor = 450

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()

#DELETE

# nome_produto = "peça_pc"

# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()