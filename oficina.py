from flask import Flask, render_template, request, redirect, url_for, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='AutoTech Serviços',
                         version='1.0.0', )
spec.register(app)

@app.route('/clientes', methods=['GET'])
def clientes():




if __name__ == '__main__':
    app.run(debug=True)