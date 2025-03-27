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

@app.route('/validadealunos')
def validado():
    try:
        prazo = 12
        meses = datetime.today()+relativedelta(months=prazo)
        # years=
        anos = datetime.now()+relativedelta(years=prazo)
        # weeks=
        semanas = ''
        # days=
        dias = ''

        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
                f'"Antes" - {datetime.today().strftime("%d-%m-%Y")}, '
                f'"Prazo" - {prazo}, '
                f'"Dias"- {dias}, '
                f'"Semanas"- {semanas}, '
                f'"Meses"- {meses},'
                f'"Anos"- {anos}'
        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)