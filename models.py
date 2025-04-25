from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

# Configuração com a conexão com o banco de dados
engine = create_engine('sqlite:///atividades.sqlite3')

# Gerencia as sessões com o banco de dados
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()



# Base_declarativa - Ela permite que você defina classes Python que representam tabelas de
# banco de dados de forma declarativa, sem a necessidade de configurar manualmente a
# relação entre as classes e as tabelas.


# Ordens e serviços
class Veiculo(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    cliente_associado = Column(String(100), nullable=False, index=True)
    modelo = Column(String(100), nullable=False, index=True)
    placa = Column(String(100), nullable=False, index=True)
    ano_fabricacao = Column(Integer, nullable=False, index=True)
    marca = Column(String(100), nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Veiculo: {} {} {} {} {}>'.format(self.cliente_associado,
                                                  self.modelo,
                                                  self.placa,
                                                  self.ano_fabricacao,
                                                  self.marca)

    # Função para salvar no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar no banco
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    # Coloca os dados na tabela
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
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, index=True)
    cpf = Column(Integer, nullable=False, index=True)
    telefone = Column(Integer, nullable=False, index=True)
    endereco = Column(String(100), nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Cliente: {} {} {} {}>'.format(self.nome,
                                            self.cpf,
                                            self.telefone,
                                            self.endereco)

    # Função para salvar no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

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
    __tablename__ = 'ordens'
    id = Column(Integer, primary_key=True)
    veiculo_associado = Column(String(100), nullable=False, index=True)
    data_abertura = Column(String(100), nullable=False, index=True)
    descricao_servico = Column(String(100), nullable=False, index=True)
    status = Column(String(100), nullable=False, index=True)
    valor_estimado = Column(Integer, nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Ordem: {} {} {} {} {}>'.format(self.veiculo_associado,
                                                         self.data_abertura,
                                                         self.descricao_servico,
                                                         self.status,
                                                         self.valor_estimado)
    # Função para salvar
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

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