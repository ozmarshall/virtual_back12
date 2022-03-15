from flask import Flask, request
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app=app, origins=['http://127.0.0.1:5500', 'https://www.mifrontend.com',
     'https://miapp.vercel.app'], methods='*', allow_headers=['Content-Type'])


clientes = [
    {
        "nombre": "PEDRO",
        "pais": "PERU",
        "edad": 12,
        "id": 1,
        "organos": False,
        "casado": False
    }
]


def buscar_usuario(id):
    # iterar la lista y buscaremos el cliente por ese id y si no existe imprimir un mensaje
    # v1
    # for cliente in clientes:
    #     if cliente.get('id') == id:
    #         return cliente
    # v2
    for posicion in range(0, len(clientes)):
        cliente = clientes[posicion]
        if cliente.get('id') == id:
            return (cliente, posicion)


@app.route('/')
def estado():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%d/%m/%y %H:%M:%S'),
        'message': 'hora actualizada'
    }





@app.route('/clientes', methods=['POST', 'GET'])
@cross_origin(origins=['http://127.0.0.1:7000', 'http://mipagina.com'])
def obtener_clientes():

    print(request.method)
    print(request.data)
    print(request.get_json())
    if request.method == 'POST':

        data = request.get_json()
        data['id'] = len(clientes) + 1
        clientes.append(data)

        return {
            'message': 'cliente agragado exitosamnete',
            'cliente': data
        }
    else:
        return {

            'message': 'la lista de clientes',
            'cliente': clientes
        }


@app.route('/cliente/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_usuario(id):
    print(id)
    if request.method == 'GET':
        cliente = buscar_usuario(id)
        if cliente:
            return cliente[0]
        else:
            return {
                'message': 'el usuario a buscar no se encontro'
            }, 404

    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado is not None:
            # hacemos la destructuracion de nuestra tupla creando las variables cliente y posicion
            [cliente, posicion] = resultado

            # cliente = resultado[0]
            # posicion = resultado[1]

            # modificar el cliente
            # extraemos la informacion del body y la almacenamos en una variable
            data = request.get_json()
            # en ese diccionario agregaremos una llave 'id' y almacenaremos el id del cliente que esta en la posicion 0 de la tupla del cliente encontrado
            data['id'] = id
            # extraeremos la posicion del cliente devuelta en la posicion 1 de la tupla de buscar_cliente
            # posicion = resultado[1]
            # modificar ese cliente con el nuevo valor
            clientes[posicion] = data
            return clientes[posicion]
        else:
            return {
                'message': 'El cliente a modificar no se encontro'
            }, 404
    elif request.method == 'DELETE':  # else:
        # eliminar ese cliente luego de validar si existe o no usando el metodo validar_usuario(id) si no existe indicar lo mismo 'cliente a eliminar no se encontro'
        resultado = buscar_usuario(id)
        if resultado:
            [cliente, posicion] = resultado
            cliente_eliminado = clientes.pop(posicion)
            return {
                'message': 'Cliente eliminado exitosamente',
                'cliente': cliente_eliminado
            }
        else:
            return {
                'message': 'El cliente a eliminar no se encontro'
            }, 404


app.run(debug=True)
