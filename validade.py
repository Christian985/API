# Importar biblioteca
from flask import Flask, jsonify
# Importe para documentação
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [Flask routes] para listar rotas da API

# Criar variável para receber a classe Flask
app = Flask(__name__)

# Documentação OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

# Rota
@app.route('/validadealunos/<ano>-<mes>-<dia>/<qtd>/<tipo>', methods=['GET'])
def validado(ano, mes, dia, qtd, tipo):
    try:
        # Diferença em dias/meses/anos
        prazo = 5

        data_atual = datetime.now()

        # Converter a string da data para formato datetime
        cadastro_produto = datetime(int(ano), int(mes), int(dia)).date()
        # validade = datetime(int(2028), int(2), int(25)).date()

        if tipo == 'dia':
            dias = datetime.today().date() + relativedelta(days=int(qtd))
        elif tipo == 'mes':
            meses = datetime.today().date() + relativedelta(months=int(qtd))
        elif tipo == 'ano':
            dias = datetime.today().date() + relativedelta(days=prazo)

        # Years
        anos = datetime.today().date() + relativedelta(years=prazo)

        # Months
        meses = datetime.today().date() + relativedelta(months=prazo)

        # Days
        dias = datetime.today().date() + relativedelta(days=prazo)

        validade = datetime.today().date() + relativedelta(anos, meses, dias)

        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
            'Validade': validade.strftime('%Y/%m/%d'),

            "Data atual": data_atual.strftime("%Y/%m/%d"),

            "prazo": str(cadastro_produto),

        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400



# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)