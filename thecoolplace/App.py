from Model.Usuario import Usuario
import sqlite3
conn = sqlite3.connect ( ' usuário.db ' )
cursor = conn.cursor ()

# Criando tabela Usuario
cursor.execute ( "" "
CREATE TABLE usuario ()
    id int NOT NULL,
    nome varchar (100) NOT NULL,
    email varchar (100) NOT NULL,
    senha varchar (50) NOT NULL,
    sexo VARCHAR (10) NÃO Nulo,
    cidade VARCHAR (150) NÃO NULL,
    data_nascimento DATA NÃO NULL,
    );
"" " )
print ( ' tabela criada ' )
# Finalizando criacao da tabela usuário

# inserir usuário
cursor.execute ( "" "
Insira no usuário (id, nome, email, senha, sexo, cidade, data_nascimento)
valores (2, 'nicolas', nicolas @ gmail ',' 12345 ',' masculino ',' soledade ', 2001/08/30)
"" " )

# selecionar usuário
cursor.execute ( "" "
selecione * do usuário
"" " )

para linha em cursor.fetchall ():
    imprimir (linha)

id_usuario =  1

# update usuário
cursor.execute ( "" " "
Atualizar usuário
onde id =?
"" " , (id_usuario,))

print ( ' dados atualizados ' )

# delete user
cursor.execute ( "" " "
eliminar do usuário
onde id =?
"" " , (id_usuario,))

#tabela usuario
select * from [TB_usuario]
delet from [TB_usuario] where id = ?
update [TB_usuario] set (id_usuario) values(?) where id = ?

# Criando tabela Mensagem
cursor.execute ( "" "
CREATE TABLE mensagem (
    id int NOT NULL,
    destinatario varchar (150) NÃO NULL,
    rementente varchar (150) NOT NULL,
    data_envio data NÃO NULL
    );
"" " )
print ( ' tabela criada ' )

# inserir mensagem
cursor.execute ( "" " "
inserir na mensagem (id, destinatario, rementente, data_envio)
valores (3'nicolas ',' stefani ', 2017/10/25)
"" " )

# selecionar mensagem
cursor.execute ( "" "
selecione * da mensagem
"" " )

para linha em cursor.fetchall ():
    imprimir (linha)

id_mensagem =  6

# atualização mensagem
cursor.execute ( "" "
mensagem de atualização
onde id =?
"" " , (id_mensagem,))
print ( ' Dados atualizados ' )

# delete message
cursor.execute ( "" "
excluir da mensagem
onde id =?
"" " , (id_mensagem,))

select * from [TB_mensagem]
delet from [TB_mensagem] where id = ?
update [TB_mensagem] set (id_mensagem) values(?) where id = ?


# criando um conversor de tabela
cursor.execute ( "" "
CREATE TABLE chat (
    conversa varchar (100) NOT NULL,
    id int NOT NULL
    );
"" " )
print ( ' Tabela criada! ' )

# inserir bate-papo
cursor.execute ( "" "
Insira no chat (conversa, id)
valores ('oi', 7)
"" " )

# selecione o bate-papo
cursor.execute ( "" "
selecione * a partir do chat
"" " )

para linha em cursor.fetchall ():
    imprimir (linha)

id_chat =  9

# atualização
cursor.execute ( "" "
atualizar conversa
onde id =?
"" " , (id_chat,))
print ( ' dados atualizados ' )

# delete chat
cursor.execute ( "" " "
excluir do bate-papo
onde id =?
"" " , (id_chat,))

select * from [TB_chat]
delet from [TB_chat] where id = ?
update [TB_chat] set (id_chat) values(?) where id = ?

# criando uma alimentação de tabela
cursor.execute ( "" " "
Criar alimentação de tabela (
    publicaçao varchar (500) não nulo,
    id int null
    );
"" " )
print ( ' Tabela criada ' )

# inserir feed
cursor.execute ( "" "
inserir no feed (publicacao, id)
valores ('publicacao', 5)
"" " )

# selecione o feed
cursor.execute ( "" " "
selecione * do feed
"" " )

para linha em cursor.fetchall ():
    imprimir (linha)


id_feed =  4

# atualização de feed
cursor.execute ( "" "
feed de atualização
onde id =?
"" " , (id_feed,))
print ( ' dados atualizados ' )

# delete feed
cursor.execute ( "" " "
excluir do feed
onde id =?
"" " , (id_feed,))

select * from [TB_feed]
delet from [TB_feed] where id = ?
update [TB_feed] set (id_feed) values(?) where id = ?


# criando tabela visibiliade
cursor.execute ( "" " "
criar tabela de visibilidade (
    publica varchar (100) não nulo,
    id int null,
    privado varchar (100) não é nulo
    );
"" " )
print ( ' tabela criada ' )

# inserção visual
cursor.execute ( "" " "
inserir na visibilidade (publica, id, privada)
valores ('visivel', 20, 'privado')
"" " )

cursor.execute ( "" "
selecione * da visibilidade
"" " )

para linha em cursor.fetchall ():
    imprimir (linha)


id_visibilidade =  30

# update visibiliade
cursor.execute ( "" " "
atualizar a visibilidade
onde id =?
"" " , (id_visibilidade,))
print ( ' dados atualizados ' )

# delete visibiliade
cursor.execute ( "" " "
excluir da visibilidade
onde id =?
"" " , (id_visibilidade,))
conn.commit ()
conn.close ()

select * from [TB_visibilidade]
delet from [TB_visibilidade] where id = ?
update [TB_visibilidade] set (id_visibilidade) values(?) where id = ?

'''
CRIANDO O MENU
'''
        print("Menu:\n "
              "1- Criar rede social\n"
              "2- Inserir usuário\n"
              "3- Adicionar amigo\n"
              "4- Enviar mensagem\n")
        try:
            op = input("Digite a opção desejada: ")

            if op == 1:
               criarRedeSocial()
            elif op == 2:
                inserirUsuario()
            elif op == 3:
                adicionarAmigo()
            elif op == 4:
                enviarMensagem()
                break

        except ValueError:
            print("Só números são válidos... Tente novamente!")


if __name__ == '__main__':
    main()
