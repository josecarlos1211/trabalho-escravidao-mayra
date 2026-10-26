from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chegada-africanos')
def chegada_africanos():
    return render_template('chegada-africanos.html')
@app.route('/trabalho-vida')
def trabalho_vida():
    return render_template('trabalho-vida.html')
@app.route('/resistencia-quilombos')
def resistencia_quilombos():
    return render_template('resistencia-quilombos.html')
@app.route('/abolicao-escravidao')
def abolicao_escravidao():
    return render_template('abolicao-escravidao.html')
@app.route('/legado-africano')
def legado_africano():
    return render_template('legado-africano.html')

if __name__ == '__main__':
    app.run(debug=True)
