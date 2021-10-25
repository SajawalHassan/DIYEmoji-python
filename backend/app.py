from flask import Flask, request, jsonify, Response
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Img

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db_init(app)

@app.route('/', methods=["GET"])
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


@app.route('/api/photos/<int:id>', methods=["GET"])
def get_image(id):
    img = Img.query.filter_by(id=id).first()

    if not img:
        return jsonify({ "msg":"No img found" }), 404

    return Response(img.img, mimetype=img.mimetype)


@app.route('/api/photos/<int:id>', methods=["DELETE"])
def delete_image(id):
    img = Img.query.filter_by(id=id).delete()

    if not img:
        return jsonify({ "msg":"No img found to delete" }), 404

    return jsonify({ "msg": "Image Deleted" }), 200


if __name__ == "__main__":
    app.run(debug=True)