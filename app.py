from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey, we have Flask in a Docker container!'

@app.route('/alura')
def inicio():
    return render_template('base.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')