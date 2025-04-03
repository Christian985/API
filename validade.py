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


@app.route('/validadealunos/<ano>-<mes>-<dia>', methods=['GET'])
def validado(ano, mes, dia):
    try:
        prazo = 12

        data_atual = datetime.now()
        # Converter a string da data para formato datetime
        cadastro = datetime(int(ano), int(mes), int(dia)).date()

        # Years =
        anos = datetime.today().date() - relativedelta(years=prazo)

        # Months
        meses = datetime.today().date() - relativedelta(months=prazo)

        # Weeks =
        semanas = datetime.today().date() - relativedelta(weeks=prazo)

        # Days =
        dias = datetime.today().date() - relativedelta(days=prazo)






        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
                "Antes":  str(datetime.today().strftime("%Y-%m-%d")),

                "data_atual": data_atual.strftime("%d-%m-%Y"),

                "Cadastro": str(cadastro),

                "Dias": str(dias),

                "Semanas": str(semanas),

                "Meses": str(meses),

                "Anos": str(anos)
        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400



# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)