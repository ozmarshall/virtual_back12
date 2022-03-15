from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngesdioentesController

app = Flask(__name__)
#se crea la instancia de flask_redsful.Api y e indicamos que toda la cinfiguracion que haremos se agregue a nuestra instancoia de flask
api = Api(app=app)

@app.route('/status', methods= ['GET'])
def status():
    return {
        'status': True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:$S')
    }




api.add_resource(IngesdioentesController, '/ingredientes', '/ingrediente')




if __name__== '__main__':
    app.run(debug=True)