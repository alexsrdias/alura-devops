from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey, we have Flask in a Docker container!'

@app.route('/alura')
def inicio():
    lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    return render_template('base.html', titulo='Jogos do Alex Dias', jogos=lista)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9999)