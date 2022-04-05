
from flask_restful import Resource, request
from dtos.registro_dto import RegistroDto, UsuarioResponseDTO, LoginDTO
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion, sendgrid
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import environ
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import json 

#from sendgrid.helpers.mail import Email, To, Content, Mail


class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDto().load(body)
            nuevoUsuario = Usuario(**data)
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)

            return {
                'message': 'Usuario registrado exitosamente',
                'content': respuesta
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al registrar usuario',
                'content': e.args
            }, 400


class LoginController(Resource):
    def post(self):
        body = request.get_json()

        try:
            data = LoginDTO().load(body)
            return {
                'message': 'Bienvenido'
            }

        except Exception as e:
            return {
                'message': 'Credenciales incorrectas',
                'content': e.args
            }


class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        # --------------------------------python
        mensaje = MIMEMultipart()

        email_emisor = 'ederiveroman@gmail.com'# environ.get('EMAIL_EMISOR')
        email_password ='slrqzezyzrplhkrr'# environ.get('EMAIL_PASSWORD')

        try:
            data = ResetPasswordRequestDTO().load(body)
            # validar si existe ese usuario en mi bd
            usuarioEncontrado = conexion.session.query(
                Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                # texto = "Hola, este es un mensaje de prueba."
                mensaje['Subject'] = 'Reiniciar contraseña Monedero APP'


                fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
                mensaje_secreto = {
                    'fecha_caducidad':  str(datetime.now()+timedelta(hours=1)),
                    'id_usuario' : usuarioEncontrado.id
                }

                mensaje_secreto_str = json.dumps(mensaje_secreto)
                mensaje_encryptado = fernet.encrypt(bytes(mensaje_secreto_str, 'utf-8'))




                # si queremos un generador de correos con diseño : https://beefree.io/
                html = open('./email_templates/joshua_template.html').read().format(
                    usuarioEncontrado.nombre, environ.get('URL_FRONT')+'/reset-password?token='+mensaje_encryptado.decode('utf-8'))

                #mensaje.attach(MIMEText(texto, 'plain'))
                mensaje.attach(MIMEText(html, 'html'))
                print(email_emisor)
                #inicio de Correo
                emisorSMTP=SMTP('smtp.gmail.com',587)
                emisorSMTP.starttls()
                emisorSMTP.login(email_emisor, email_password)

                emisorSMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=usuarioEncontrado.correo,
                    msg=mensaje.as_string()
                )
                emisorSMTP.quit()

            return {
                'message': 'Correo enviado exitosamente'
            }
        except Exception as e:
            print(e)
            return {
                'message': 'Error al enviar correo',
                'content': e.args
            },400


# --------------------------------python
        # try:
        #     data = ResetPasswordRequestDTO().load(body)
        #     usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
        #     if usuarioEncontrado is not None:

        #         from_email = Email('peter.redskin@gmail.com')
        #         to_email = To(usuarioEncontrado.correo)
        #         subject = 'Reinicia tu contgraseña del Monedero App'
        #         content = Content('text/plain', 'hola, has solicitado el reinicio de tu contraseña, haz clic en le link para cambiar, si no has sido tu ignora este mensaje:....')
        #         mail = Mail(from_email, to_email, subject, content)
        #         envia_correo = sendgrid.client.mail.send.post (request_body=mail.get())

        #         print(envia_correo.status_code)
        #         print(envia_correo.body)
        #         print(envia_correo.headers)

        #     return {
        #         'message' : 'Revise su correo'
        #     }

        # except Exception as e:
        #     print(e)
        #     return {
        #         'message' : 'Error al resetear la password',
        #         # 'content': e.args
        #     }
