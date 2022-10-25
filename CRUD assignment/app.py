from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
# load python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

GCP_MYSQL_HOSTNAME = os.getenv('GCP_MYSQL_HOSTNAME')
GCP_MYSQL_USER = os.getenv('GCP_MYSQL_USER')
GCP_MYSQL_PASSWORD = os.getenv('GCP_MYSQL_PASSWORD')
GCP_MYSQL_DATABASE = os.getenv('GCP_MYSQL_DATABASE')

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + GCP_MYSQL_USER+ ':' + GCP_MYSQL_PASSWORD + '@' + GCP_MYSQL_HOSTNAME + ':3306/patient_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '87378742'

db.init_app(app)




###Models

class Patients(db.Model):
    __tablename__ = 'production_patients'

    id = db.Column(db.Integer, primary_key=True)
    mrn = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    # this first function __init__ is to establish the class for python GUI
    def __init__(self, mrn, first_name, last_name):
        self.mrn = mrn
        self.first_name = first_name
        self.last_name = last_name

    # this second function is for the API endpoints to return JSON 
    def to_json(self):
        return {
            'id': self.id,
            'mrn': self.mrn,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)