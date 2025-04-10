from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///nome.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# Método para criar banco
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

# Base_declarativa - Ela permite que você defina classes Python que representam tabelas de
# banco de dados de forma declarativa, sem a necessidade de configurar manualmente a
# relação entre as classes e as tabelas.

class Ativadade(Base):
    __tablename__ = 'ativadade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    clientes = relationship('Cliente')

class Veiculo():
    __tablename__ = 'Veiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    marca = Column(String(100), nullable=False, index=True)

class Cliente():
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

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
        'id': self.id,
        'nome': self.nome,
        'email': self.email,
        'marca': self.marca
    }
    return dados_user

