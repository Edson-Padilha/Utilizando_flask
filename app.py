from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify ({'id':id,'nome':'Edson', 'profissao':'Desenvolvedor'})


@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    return jsonify({'soma':valor1 + valor2})

if __name__ == '__main__':
    app.run(debug=True)
