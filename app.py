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
# Exemplo
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

        # Converter a string da data para formato datetime
        data_recebida = datetime(int(ano), int(mes), int(dia)).date()

        # Irá diferenciar os dias
        dias_diferenca = data_recebida.day - data_atual.date().day

        # Irá diferenciar os meses
        meses_diferenca = data_recebida.month - data_atual.date().month

        # Irá diferenciar os anos
        anos_diferenca = data_recebida.year - data_atual.date().year

        situacao = ''

        # Irão preencher a variável 'situacao'
        if data_recebida > data_atual.date():
            situacao = 'Futuro'

        elif data_recebida < data_atual.date():
            situacao = 'Passado'

        elif data_recebida == data_atual.date():
            situacao = 'Presente'



        # Irá retornar o Jsonify e mostrará os resultados
        return jsonify({
            'Situacao': situacao,
            'Diferenca de dias': str(abs(dias_diferenca)),
            'Diferenca de meses': str(abs(meses_diferenca)),
            'Diferenca de anos': str(abs(anos_diferenca)),
        })
    # Caso o valor escrito esteja errado
    except ValueError:
        return jsonify({'Erro': 'Formato de data incorreto'}), 400


if __name__ == '__main__':
    app.run(debug=True)
