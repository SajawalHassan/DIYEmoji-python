from os import name
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Img

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db_init(app)

@app.route('/')
def index():
    return 'Hello Wolrd'


@app.route('/api/photos', methods=['POST'])
def upload():
    file = request.files['file']

    if not file:
        return jsonify({ "msg":"No file uploaded, there was no file to upload"  }), 400

    filename = secure_filename(file.filename)
    mimetype = file.mimetype
 
    img = Img(img=file.read(), mimetype=mimetype, name=filename)
    db.session.add(img)
    db.session.commit()

    return jsonify({ "msg":f"Image has been uploaded with the filename of {filename}" }), 200



if __name__ == "__main__":
    app.run(debug=True)