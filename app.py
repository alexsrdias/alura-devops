from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'fcf69511f5b3c2006c8106472c7a485b'


class Jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome 
    self.categoria = categoria 
    self.console = console

class User:
  def __init__(self, id, name, password):
    self.id = id 
    self.name = name 
    self.password = password

jogo1 = Jogos('Super Mario', 'Acao', 'SNES')
jogo2 = Jogos('Dinossauro Cadilac', 'Aventura', 'ARCADE')
jogo3 = Jogos('Uncharted 4', 'Aventura', 'PS4')
lista = [jogo1, jogo2, jogo3]

user1 = User('asrd', 'Alex Dias', '123')
user2 = User('msrd', 'Marcelo Dias', '231')
user3 = User('vsrd', 'Vivian Dias', '312')


# Rotas de Paginas

# Rota - index
@app.route('/')
@app.route('/index')

def index():
  
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect('/login?page=index')
  else:
    return render_template('home.html', titulo='Jogos do Alex Dias', jogos=lista)

# Rota de Novo Elemento
@app.route('/novo')
def novo():
  
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', page=url_for('novo')))
    else:
      return render_template('form.html', titulo='Novo jogo')

# Rota de Login
@app.route('/login')
def login():
  page = request.args.get('page')
  return render_template('login.html', page=page )

# Rota de Logout
@app.route('/logout')
def logout():
  
  session ['usuario_logado']=None
  
  flash('Não está Logado')

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

    return redirect(url_for('index'))
  
# Rota de Serviço de Atenticar  
@app.route('/auth', methods=['POST'])
def auth():

  if '123' == request.form['senha']:

    session ['usuario_logado'] = request.form['usuario']
    flash(request.form['usuario'] + ' logou com sucesso!')
    page = request.form['page']

    return redirect(page)

  else :

    flash('Não logado, tente de novo!')

    return redirect (url_for('login'))

# Verificar se esta logado
def check_login():

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9999)