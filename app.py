from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():

    return render_template('inicio.jinja', nombre='pedro', dia='jueves', integrantes=[
        'Foca',
        'Lapagol',
        'Ruidiaz',
        'Paolin',
        'Rayo Advincula'
    ], usuario= {
        'nombre': 'Juan',
        'direccion': 'las piedritas 105',
        'edad': '40'
    }, selecciones = [{
        'nombre': 'Bolivia',
        'clasificado': True
    },{
        'nombre': 'Brasil',
        'clasificado': True
    },{
        'nombre': 'Chile',
        'clasificado': False
    },{
        'nombre': 'Peru',
        'timado': True
    }])

if(__name__== '__main__'):
    app.run(debug=True)

