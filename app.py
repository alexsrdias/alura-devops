from flask import Flask, render_template

app = Flask(__name__)


class Jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome 
    self.categoria = categoria 
    self.console = console


@app.route('/')
def hello_world():
  return 'Hey, we have Flask in a Docker container!'

@app.route('/alura')
def inicio():
    jogo1 = Jogos('Super Mario', 'Acao', 'SNES')
    jogo2 = Jogos('Dinossauro Cadilac', 'Aventura', 'ARCADE')
    jogo3 = Jogos('Uncharted 4', 'Aventura', 'PS4')
    lista = [jogo1, jogo2, jogo3]
    return render_template('base.html', titulo='Jogos do Alex Dias', jogos=lista)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9999)