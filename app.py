from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome 
    self.categoria = categoria 
    self.console = console

jogo1 = Jogos('Super Mario', 'Acao', 'SNES')
jogo2 = Jogos('Dinossauro Cadilac', 'Aventura', 'ARCADE')
jogo3 = Jogos('Uncharted 4', 'Aventura', 'PS4')
lista = [jogo1, jogo2, jogo3]


# Rotas de Paginas

# Rota - index
@app.route('/')
def index():

    return render_template('home.html', titulo='Jogos do Alex Dias', jogos=lista)

# Rota de Novo Elemento
@app.route('/novo')
def novo():
    return render_template('form.html', titulo='Novo Jogo')


# Rota de Login
@app.route('/login')
def login():
    return render_template('login.html')

#
# Rotas de Serviços
#

# Rota de Serviço para Criar
@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')
  
# Rota de Serviço de Atenticar  
@app.route('/auth', methods=['POST'])
def auth():
  if '123' == request.form['senha']:
    return redirect('/')
  else :
    return redirect ('/login')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9999)