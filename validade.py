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
        # Converter a string da data para formato datetime
        cadastro_produto = datetime(int(ano), int(mes), int(dia)).date()

        if tipo == 'dia':
            validade = cadastro_produto + relativedelta(days=int(qtd))
        elif tipo == 'mes':
            validade = cadastro_produto + relativedelta(months=int(qtd))
        elif tipo == 'ano':
            validade = cadastro_produto + relativedelta(years=int(qtd))
        else:
            return jsonify({
                'Mensagem': 'Erro de tipo',
            })



        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
            'Validade': validade.strftime('%Y/%m/%d'),

            "Data_fabricacao": cadastro_produto.strftime("%Y/%m/%d"),

            "Prazo": int(qtd),

            'Tipo': tipo,

        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400



# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)