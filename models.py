from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

# Configuração com a conexão com o Banco de Dados
engine = create_engine('sqlite:///atividades.sqlite3')

# Gerencia as sessões com o Banco de Dados
db_session = scoped_session(sessionmaker(bind=engine))


# Base_declarativa - Ela permite que você defina Classes Python que representam tabelas de
# Banco de Dados de forma declarativa, sem a necessidade de configurar manualmente a
# relação entre as Classes e as Tabelas.
Base = declarative_base()
Base.query = db_session.query_property()




# Veículos
class Veiculo(Base):
    # Tabela de Veículos
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    cliente_associado = Column(String(100), nullable=False, index=True)
    modelo = Column(String(100), nullable=False, index=True)
    placa = Column(String(100), nullable=False, index=True)
    ano_fabricacao = Column(Integer, nullable=False, index=True)
    marca = Column(String(100), nullable=False, index=True)

    # Representação de Classe
    def __repr__(self):
        return '<Veiculo: {} {} {} {} {}>'.format(self.cliente_associado,
                                                  self.modelo,
                                                  self.placa,
                                                  self.ano_fabricacao,
                                                  self.marca)

    # Função para Salvar no Banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para Deletar no Banco
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    # Coloca os Dados na Tabela
    def serialize_user(self):
        dados_user ={
            'cliente_associado': self.cliente_associado,
            'modelo': self.modelo,
            'placa': self.placa,
            'ano_fabricacao': self.ano_fabricacao,
            'marca': self.marca,
        }
        return dados_user


# Cliente
class Cliente(Base):
    # Tabela de Clientes
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, index=True)
    cpf = Column(Integer, nullable=False, index=True)
    telefone = Column(Integer, nullable=False, index=True)
    endereco = Column(String(100), nullable=False, index=True)

    # Representação Classe
    def __repr__(self):
        return '<Cliente: {} {} {} {}>'.format(self.nome,
                                            self.cpf,
                                            self.telefone,
                                            self.endereco)

    # Função para Salvar no Banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para Deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    # Função para Serializar
    def serialize_user(self):
        dados_user = {
            'id_user': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'endereco': self.endereco,
        }
        return dados_user


# Atividade
class Atividade(Base):
    # Tabela de Atividades
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    cpf = Column(Integer)
    endereco = Column(String(80))
    telefone = Column(Integer)
    veiculo_associado = Column(String(80))
    cliente_associado = Column(String(80))
    modelo = Column(String(80))
    placa = Column(String(80))
    ano_fabricacao = Column(String(80))
    marca = Column(String(80))
    status = Column(String(80))
    data_abertura = Column(String(80))
    valor_estimado = Column(String(80))

    # Id das Entidades
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    clientes = relationship('Cliente')
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'))
    veiculos = relationship('Veiculo')
    ordem_id = Column(Integer, ForeignKey('ordens.id'))
    ordens = relationship('Ordem')


# Ordens e Serviços
class Ordem(Base):
    # Tabela de Ordens e Serviços
    __tablename__ = 'ordens'
    id = Column(Integer, primary_key=True)
    veiculo_associado = Column(String(100), nullable=False, index=True)
    data_abertura = Column(String(100), nullable=False, index=True)
    descricao_servico = Column(String(100), nullable=False, index=True)
    status = Column(String(100), nullable=False, index=True)
    valor_estimado = Column(Integer, nullable=False, index=True)

    # Representação de Classe
    def __repr__(self):
        return '<Ordem: {} {} {} {} {}>'.format(self.veiculo_associado,
                                                         self.data_abertura,
                                                         self.descricao_servico,
                                                         self.status,
                                                         self.valor_estimado)
    # Função para Salvar
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para Deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    # Função para Serializar
    def serialize_user(self):
        dados_user = {
            'veiculo_associado': self.veiculo_associado,
            'data_abertura': self.data_abertura,
            'descricao_servico': self.descricao_servico,
            'status': self.status,
            'valor_estimado': self.valor_estimado,
        }
        return dados_user


# Método para criar banco
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()