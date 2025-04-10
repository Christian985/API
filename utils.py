from models import Cliente, db_session
from sqlalchemy import select


# Inserir dados na tabela
def inserir_cliente():
    cliente = Cliente(nome=str(input('Nome: ')),
                      email=str(input('E-Mail: '))
                      )
    print(cliente)
    cliente.save()

def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)
    if __name__ == '__main__':
        consultar_cliente()
        # run()

def atualizar_cliente():
    # Seleciona o item a ser alterado
    var_cliente = select(Cliente).where(str(input('Nome: ')) == Cliente.nome)
    var_cliente = db_session.execute(var_cliente).scalar()
    # Nova informação
    var_cliente.nome = str(input('Novo Nome: '))
    var_cliente.save()

def deletar_cliente():
    cliente_deletar = input('Quem você deseja deletar? :')
    var_cliente = select(Cliente).where(cliente_deletar == Cliente.nome)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()

if __name__ == '__main__':

    while True:
        print('Menu')
        print('1 - Inserir Cliente')
        print('2 - Consultar Cliente')
        print('3 - Atualizar Cliente')
        print('4 - Deletar Cliente')
        print('5 - Sair')
        escolha = input('Escolha: ')
        if escolha == '1':
            inserir_cliente()
        elif escolha == '2':
            consultar_cliente()
        elif escolha == '3':
            atualizar_cliente()
        elif escolha == '4':
            deletar_cliente()
        elif escolha == '5':
            break