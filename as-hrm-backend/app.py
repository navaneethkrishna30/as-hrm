from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'db.db')
app.config['SECRET_KEY'] = 'ashrm123'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getStates', methods=['GET','POST'])
def getStates():
    return {
        'states':['Telangana', 'andhra pradesh', 'Karnataka']
    }

if __name__ == "__main__":
    app.run(debug=True)