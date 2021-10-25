from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from db import db_init

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db_init(app)

if __name__ == "__main__":
    app.run(debug=True)