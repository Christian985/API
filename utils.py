from model import Cliente, db_session
from sqlalchemy import select

def inserir_cliente():
    cliente = Cliente(nome=str(input('Nome: ')),
                      email=str(input('E-Mail: '))
                      )
    print(cliente)
    cliente.save()

def consultar_cliente():

def atualizar_cliente():

def deletar_cliente():