from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)


class check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    memory = db.Column(db.String(80),unique=False)
    cpu = db.Column(db.String(80),unique=False)
    disk = db.Column(db.String(80),unique=False)
    ssh = db.Column(db.String(80),unique=False)

    def __init__(self, memory, cpu, disk, ssh):
        self.memory = memory
        self.cpu = cpu
	self.disk= disk
	self.ssh = ssh

    def __repr__(self):
        return '<Checks: memory=%r, cpu=%r, disk=%r, sshd=%r>' % (self.memory,self.cpu,self.disk,self.ssh)

class checkSchema(ma.ModelSchema):
    class Meta:
	model = check 
