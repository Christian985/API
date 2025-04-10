from flask import Flask, render_template, request, redirect, url_for, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='AutoTech Serviços',
                         version='1.0.0', )
spec.register(app)

@app.route('/clientes', methods=['GET'])
def clientes():
    __tablename__ = 'clientes'
    id = db.Collumn(db.Integer, primary_key=True)
    nome = db.Collumn(db.String(100), nullable=False)
    email = db.Collumn(db.String(100), nullable=False)




@app.route('/veiculos', methods=['GET'])
def veiculos():
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Collumn(db.String(100), nullable=False)
    marca = db.Collumn(db.String(100), nullable=False)



@app.route('/ordem', methods=['GET'])
def ordens_servicos():
    return ('ordems')


if __name__ == '__main__':
    app.run(debug=True)