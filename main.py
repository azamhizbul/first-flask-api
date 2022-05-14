# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from Modules.example.hello import Hello
from Modules.example.square import Square

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

hello = Hello
square = Square

api.add_resource(hello, '/')
api.add_resource(square, '/square/<int:num>')


# driver function
if __name__ == '__main__':
  
    app.run(debug = True)