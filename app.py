from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0',)
spec.register(app)


@app.route('/dias/<data_str>', methods=['GET'])
def dias_valores(data_str):
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
        data_entrada = datetime.strptime(data_str, "%d/%m/%Y") # "%Y-%m-%d"
    except ValueError:
        return jsonify({"erro": "Formato de data incorreto"}), 400
# Tempo atual
@app.route('/dia_atual')
def dia_atual():
    atual = datetime.datetime.now()
    atual = atual.strftime('%d/%m/%Y | %H:%M:%S')
    return jsonify({"Tempo atual": atual}), 200




if __name__ == '__main__':
    app.run(debug=True)