from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base,

engine = create_engine('sqlite:///nome.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
# Base_declarativa - Ela permite que você defina classes Python que representam tabelas de
# banco de dados de forma declarativa, sem a necessidade de configurar manualmente a
# relação entre as classes e as tabelas.
Base.query = db_session.query_property()
class Veiculo():
    __tablename__ = 'Veiculos'
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Collumn(db.String(100), nullable=False)
    marca = db.Collumn(db.String(100), nullable=False)

class Cliente():
    __tablename__ = 'clientes'
    id = db.Collumn(db.Integer, primary_key=True)
    nome = db.Collumn(db.String(100), nullable=False)
    email = db.Collumn(db.String(100), nullable=False)