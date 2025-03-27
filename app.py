from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0', )
spec.register(app)

# Rota
@app.route('/dias/<ano>-<mes>-<dia>', methods=['GET'])
def data(ano, mes, dia):
# Converter a string da data para formato datetime
    """
        API para calcular a diferença entre duas datas.

        ## Endpoint:
        'GET /dias/<data_str>'

        ## Parâmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"** (exemplo: "15-03-2025").
          - **Qualquer outro formato resultará em erro.**

        ## Resposta (JSON):
        ```json
        {
            "dias": 100,
            "meses": 3,
            "anos": 0,
            "tempo": "passado"
        }
        '''

        ## Erros possíveis:
        - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
        ```json
    """

    try:
        data_atual = datetime.now()

        data_recebida = datetime(int(ano), int(mes), int(dia)).date()

        dias_diferenca = data_recebida - data_atual.date()

        meses_diferenca = data_recebida - data_atual.date()

        anos_diferenca = data_recebida - data_atual.date()

        situacao = ''

        if data_recebida > data_atual.date():
            situacao = 'Futuro'

        elif data_recebida < data_atual.date():
            situacao = 'Passado'

        elif data_recebida == data_atual.date():
            situacao = 'Presente'



        # data_entrada = datetime.strptime(data_str, "%d/%m/%Y") # "%Y-%m-%d"

        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
            'Situacao': situacao,
            'Diferenca de dias': str(dias_diferenca),
            'Diferenca de meses': str(meses_diferenca),
            'Diferenca de anos': str(anos_diferenca),
        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400


if __name__ == '__main__':
    app.run(debug=True)
