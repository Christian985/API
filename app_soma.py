from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/<name>')
def hello_name(name):
    return f'olá, {name}!'



# Soma
@app.route('/soma/<num1>+<num2>')
def soma(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'O resultado é {num1} + {num2} = {num1 + num2}'



# Subtração
@app.route('/soma/<num1>-<num2>')
def subtracao(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'O resultado é {num1} - {num2} = {num1 - num2}'



# Multiplicação
@app.route('/soma/<num1>*<num2>')
def multiplicacao(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'O resultado é {num1} * {num2} = {num1 * num2}'



# Divisão
@app.route('/soma/<num1>/<num2>')
def divisao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return f'O resultado é {num1} / {num2} = {num1 / num2}'
    except ValueError:
        return f'Digite apenas números inteiros e positivos'
    except ZeroDivisionError:
        return "Não é possivel dividir por zero."



# Par ou impar
@app.route('/par-impar/<num1>')
def valor(num1):
    num1 = int(num1)
    resultado = num1 % 2
    if resultado == 0:
        return f'O número é Par!'
    else:
        return f'O número é Impar!'



if __name__ == '__main__':
    app.run(debug=True)