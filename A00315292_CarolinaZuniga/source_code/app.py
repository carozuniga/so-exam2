import json
from flask import Flask, abort, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from database import check, db, checkSchema
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

api = Api(app,version='1.0', title='API for system checks', description='Design and implementation of microservices for the management of infrastructure tasks')


@api.route('/checks')
class ChecksView(Resource):
    @api.response(200, 'Last check successfully returned.')
    def get(self):

	ch = check.query.order_by(desc(check.id)).first()
	return checkSchema().dump(ch).data, 200
	
    def post(self):        
        return "Does not apply", 501

    def put(self):        
        return "Does not apply", 501

    def delete(self):        
        return "Does not apply", 501

@api.route('/checks/cpu/history')
class cpuHistory(Resource):

	@api.response(200, 'cpu data successfully returned.')
	def get(self):

		size= request.args.get('size')

		ch = check.query.order_by(desc(check.id)).limit(size).all()
		list = {}
		lis = []
		for i in range(len(ch)):
			c = ch[i].cpu
			lis.append(c)

		list["data"] = lis
		return json.dumps(list),200

	def post(self):        
	        return "Does not apply", 501

	def put(self):        
        	return "Does not apply", 501

    	def delete(self):        
        	return "Does not apply", 501

@api.route('/checks/memory/history')
class memoryHistory(Resource):

	@api.response(200, 'memory data successfully returned.')
	def get(self):

		size= request.args.get('size')

		ch = check.query.order_by(desc(check.id)).limit(size).all()
		list = {}
		lis = []
		for i in range(len(ch)):
			c = ch[i].memory
			lis.append(c)

		list["data"] = lis
		return json.dumps(list),200

	def post(self):        
	        return "Does not apply", 501

    	def put(self):        
        	return "Does not apply", 501

    	def delete(self):        
 		return "Does not apply", 501

@api.route('/checks/disk/history')
class diskHistory(Resource):

	@api.response(200, 'disk data successfully returned.')
	def get(self):

		size= request.args.get('size')

		ch = check.query.order_by(desc(check.id)).limit(size).all()
		list = {}
		lis = []
		for i in range(len(ch)):
			c = ch[i].disk
			lis.append(c)

		list["data"] = lis
		return json.dumps(list),200

	def post(self):        
        	return "Does not apply", 501

    	def put(self):        
        	return "Does not apply", 501

    	def delete(self):        
        	return "Does not apply", 501

@api.route('/checks/sshd/history')
class sshdHistory(Resource):

	@api.response(200, 'sshd data successfully returned.')
	def get(self):

		size= request.args.get('size')

		ch = check.query.order_by(desc(check.id)).limit(size).all()
		list = {}
		lis = []
		for i in range(len(ch)):
			c = ch[i].ssh
			lis.append(c)

		list["data"] = lis
		return json.dumps(list),200

	def post(self):        
        	return "Does not apply", 501

    	def put(self):        
        	return "Does not apply", 501

    	def delete(self):        
        	return "Does not apply", 501



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug='True')
