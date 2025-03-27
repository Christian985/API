# Importar biblioteca
from flask import Flask, jsonify, render_template

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


@app.route('/validadealunos/<ano><mes><dia>', methods=['GET'])
def validado(ano, mes, dia):
    try:
        prazo = 12

        cadastro = datetime(int(ano), int(mes), int(dia)).date()

        # Months
        meses = cadastro.today() + relativedelta(months=prazo)

        # Years =
        anos = cadastro.today() + relativedelta(years=prazo)

        # Weeks =
        semanas = cadastro.today() + relativedelta(weeks=prazo)

        # Days =
        dias = cadastro.today() + relativedelta(days=prazo)

        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
                f'"Antes" - {abs(datetime.today().strftime("%d-%m-%Y"))}, '
                f'"Cadastro"- {cadastro}, '
                f'"Dias"- {dias}, '
                f'"Semanas"- {semanas}, '
                f'"Meses"- {meses},'
                f'"Anos"- {anos} '
        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)