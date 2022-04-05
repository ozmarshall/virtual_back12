import unittest
from app import app
from datetime import datetime

class TestConfiguracion(unittest.TestCase):
    def setUp(self):
        self.aplicacion_flask = app.test_client()
        self.nombre = 'pedro'

        self.aplicacion_flask = app.test_client()


    @unittest.skip('lo salte solo para probar ')
    def testNombre(self):
        self.assertEqual(self.nombre, 'pedro')

    def testEndpointStatus(self):
        '''deberia retornar la hora del servidor y su estado'''
        respuesta = self.aplicacion_flask.get('/status')
        print(respuesta.json)

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('status'), True)
        self.assertEqual(respuesta.json.get('hora_del_servidor'), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def testLoginJWTExitoso(self):
        '''deberia retornar una token para poder ingresar a ls ruitas protegidas'''
        body = {
            'correo': 'parc.tec20@yahoo.com',
            'pass': 'pollito'
        }
        respuesta=self.aplicacion_flask.post('/login-jwt', json=body)
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('accses_token'), None)
       
        
        

    def testLoginJWTCredencialesIncorrectas(self):
        '''deberia retornar un error so las credenciales son incorrectas'''
        body = {
            'correo': 'parc.tec20@yahoo.com',
            'pass': 'Welcomevdfg'
        }
        respuesta=self.aplicacion_flask.post('/login-jwt', json=body)
        self.assertEqual(respuesta.status_code, 401)
        self.assertEqual(respuesta.json.get('accses_token'), None)
        self.assertEqual(respuesta.json.get('description'), 'Invalid credentials')

class TestYo(unittest.TestCase):
    def setUp(self):
        self.aplicacion_flask = app.test_client()
        body = {
            'correo': 'parc.tec20@yahoo.com',
            'pass': 'pollito'
        }
        respuesta=self.aplicacion_flask.post('/login-jwt', json=body)
        self.token=respuesta.json.get('access_token')


    def testNohayJWT(self):
        pass

    def testPerfil(self):
        respuesta=self.aplicacion_flask.get('/yo', headers={'Authorization': 'Bearer {}'.format(self.token)})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('message'), 'El usuario es ')
        

class TestMovimientos(unittest.TestCase):
    pass

        

        
        