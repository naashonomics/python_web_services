from flask import Flask,jsonify,request  
from flask_restful import Resource,Api 
app=Flask(__name__)
api=Api(app)

class Test(Resource):
	def get(self):
		return {'about': 'Hello World'}
	
	def post(self):
		res=request.get_json()
		return {"you sent": res },201

class  Multi(Resource):
	def get(self,num):
		return {'result':num*10}

api.add_resource(Test,'/')
api.add_resource(Multi,'/multi/<int:num>')
if __name__=='__main__':
	app.run(debug=True)