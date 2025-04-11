from models import Cliente, Veiculo, db_session, Ordem_servicos
from sqlalchemy import select
import os

# Inserir dados do Cliente na tabela
def inserir_cliente():
    cliente = Cliente(nome=str(input('Nome: ')),
                      email=str(input('E-Mail: ')),
                      endereco=str(input('Endereço: ')),
                      )
    print(cliente)
    cliente.save()


# Consultar o Cliente
def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)
    if __name__ == '__main__':
        consultar_cliente()
        # run()


# Atualiza o Cliente
def atualizar_cliente():
    # Seleciona o item a ser alterado
    var_cliente = select(Cliente).where(str(input('Nome: ')) == Cliente.nome)
    var_cliente = db_session.execute(var_cliente).scalar()
    # Nova informação
    var_cliente.nome = str(input('Novo Nome: '))
    var_cliente.save()


# Deleta o Cliente
def deletar_cliente():
    cliente_deletar = input('Quem você deseja deletar? :')
    var_cliente = select(Cliente).where(cliente_deletar == Cliente.nome)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()


# FIM DO CLIENTE


# Insere Ordem na tabela
def inserir_ordem():
    ordem_servicos = Ordem_servicos(veiculo_associado=str(input('Veículo associado: ')),
                      data_abertura=str(input('Data abertura: ')),
                      descricao_servico=str(input('Descricao servico: ')),
                      status=str(input('Status: ')),
                      valor_estimado=int(input('Valor estimado: ')),
                      )
    print(ordem_servicos)
    ordem_servicos.save()


# Consulta Ordem na tabela
def consultar_ordem():
    var_ordem = select(Ordem_servicos)
    var_ordem = db_session.execute(var_ordem).all()
    print(var_ordem)
    if __name__ == '__main__':
        consultar_ordem()
        # run()


# Atualiza Ordem na tabela
def atualizar_ordem():
    # Seleciona o item a ser alterado
    var_ordem = select(Ordem_servicos).where(str(input('Veículo associado: ')) == Ordem_servicos.veiculo_associado)
    var_ordem = db_session.execute(var_ordem).scalar()
    # Nova informação
    var_ordem.veiculo_associado = str(input('Novo Veículo associado: '))
    var_ordem.save()


# Deleta Ordem na tabela
def deletar_ordem():
    ordem_deletar = input('Quem você deseja deletar? :')
    var_ordem = select(Ordem_servicos).where(ordem_deletar == Ordem_servicos.veiculo_associado)
    var_ordem = db_session.execute(var_ordem).scalar()
    var_ordem.delete()


# FIM DA ORDEM E SERVIÇOS


# Insere o Veículo na tabela
def inserir_veiculo():
    veiculo = Veiculo(cliente_associado=str(input('Cliente associado: ')),
                      modelo=str(input('Modelo: ')),
                      placa=str(input('Placa: ')),
                      ano_fabricacao=str(input('Ano fabricacao: ')),
                      marca=str(input('Marca: ')),)
    print(veiculo)
    veiculo.save()


# Consulta o Veículo na tabela
def consultar_veiculo():
    var_veiculo = select(Veiculo)
    var_veiculo = db_session.execute(var_veiculo).all()
    print(var_veiculo)
    if __name__ == '__main__':
        consultar_veiculo()
        # run


# Atualiza o Veículo na tabela
def atualizar_veiculo():
    # Seleciona o item a ser alterado
    var_veiculo = select(Veiculo).where(str(input('Cliente associado: ')) == Veiculo.cliente_associado)
    var_veiculo = db_session.execute(var_veiculo).scalar()
    # Nova informação
    var_veiculo.cliente_associado = str(input('Novo Nome: '))
    var_veiculo.save()


# Deleta o Veículo na tabela
def deletar_veiculo():
    veiculo_deletar = input('Quem você deseja deletar? :')
    var_veiculo = select(Veiculo).where(veiculo_deletar == Veiculo.cliente_associado)
    var_veiculo = db_session.execute(var_veiculo).scalar()
    var_veiculo.delete()

# FIM DO VEÍCULO


if __name__ == '__main__':

    while True:
        print('Menu')
        print('1 - Cliente')
        print('2 - Veículo')
        print('3 - Ordens e servicos')
        print('4 - Sair')
        escolha_menu = int(input('Escolha uma opção: '))
        if escolha_menu == 1:
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

        elif escolha_menu == 2:
            print('1 - Inserir Veiculo')
            print('2 - Consultar Veiculo')
            print('3 - Atualizar Veiculo')
            print('4 - Deletar Veiculo')
            print('5 - Sair')
            escolha = input('Escolha: ')
            if escolha == '1':
                os.system('cls')
                inserir_veiculo()
            elif escolha == '2':
                os.system('cls')
                consultar_veiculo()
            elif escolha == '3':
                os.system('cls')
                atualizar_veiculo()
            elif escolha == '4':
                os.system('cls')
                deletar_veiculo()
            elif escolha == '5':
                os.system('cls')
                break

        elif escolha_menu == 3:
            print('1 - Inserir Ordem')
            print('2 - Consultar Ordem')
            print('3 - Atualizar Ordem')
            print('4 - Deletar Ordem')
            print('5 - Sair')
            escolha = input('Escolha: ')
            if escolha == '1':
                os.system('cls')
                inserir_ordem()
            elif escolha == '2':
                os.system('cls')
                consultar_ordem()
            elif escolha == '3':
                os.system('cls')
                atualizar_ordem()
            elif escolha == '4':
                os.system('cls')
                deletar_ordem()
            elif escolha == '5':
                os.system('cls')
                break