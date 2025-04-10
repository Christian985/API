from sqlalchemy import create_engine
from model import Veiculo, Cliente
from flask import Flask, render_template, request, redirect, url_for, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='AutoTech Serviços',
                         version='1.0.0', )
spec.register(app)


def validar_cliente(cliente):



@app.route('/clientes', methods=['GET'])
def clientes():





@app.route('/veiculos', methods=['GET'])
def veiculos():




@app.route('/ordem', methods=['GET'])
def ordens_servicos():
    return ('ordems')


if __name__ == '__main__':
    app.run(debug=True)