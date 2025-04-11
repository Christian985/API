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
    ano_fabricacao = Column(String(100), nullable=False, index=True)
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

    def delete(self):
        db_session.delete(self)
        db_session.commit()

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
    email = Column(String(100), nullable=False, index=True)
    endereco = Column(String(100), nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Cliente: {} {} {}>'.format(self.nome,
                                            self.email,
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
            'email': self.email,
            'endereco': self.endereco,
        }
        return dados_user


# Atividade
class Atividade(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    clientes = relationship('Cliente')
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'))
    veiculos = relationship('Veiculo')


# Ordens e Serviços
class Ordem_servicos(Base):
    __tablename__ = 'ordens e servicos'
    id = Column(Integer, primary_key=True)
    veiculo_associado = Column(String(100), nullable=False, index=True)
    data_abertura = Column(String(100), nullable=False, index=True)
    descricao_servico = Column(String(100), nullable=False, index=True)
    status = Column(String(100), nullable=False, index=True)
    valor_estimado = Column(Integer, nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Ordem_servicos: {} {} {} {} {}>'.format(self.veiculo_associado,
                                                         self.data_abertura,
                                                         self.descricao_servico,
                                                         self.status,
                                                         self.valor_estimado)

# Método para criar banco
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()