from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sql:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHMY_TRACK_MODIFICATION'] = False
# Init Database
db = SQLAlchemy(app)
# init marshmallow
ma = Marshmallow(app)


# Running the server
if __name__ == "__main__":
    app.run(debug=True)