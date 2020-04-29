from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'fcf69511f5b3c2006c8106472c7a485b'


class Jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome 
    self.categoria = categoria 
    self.console = console

class Usuario:
  def __init__(self, id, nome, senha):
    self.id = id
    self.nome = nome
    self.senha = senha

jogo1 = Jogos('Super Mario', 'Acao', 'SNES')
jogo2 = Jogos('Dinossauro Cadilac', 'Aventura', 'ARCADE')
jogo3 = Jogos('Uncharted 4', 'Aventura', 'PS4')
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario('asrd', 'Alex Dias', '123')
usuario2 = Usuario('vsrd', 'Vivian Dias', '123')
usuario3 = Usuario('msrd', 'Marcelo Dias', '123')

usuarios = { usuario1.id: usuario1, 
             usuario2.id: usuario2, 
             usuario3.id: usuario3 }

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

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
          session['usuario_logado'] = usuario.id
          flash(usuario.nome + ' logou com sucesso!')
          return redirect(request.form['page'])
        else:
          flash('Não logado, tente de novo!')
          return redirect(url_for('login'))
    else:
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))

# Verificar se esta logado
def check_login():

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9999)