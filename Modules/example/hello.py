from flask import Flask, jsonify, request
from flask_restful import Resource, Api

class Hello(Resource) :
    def get(self) :
        return jsonify({'message' : 'hello world'})

    def post(self) :
        data = request.get_json() 
        return jsonify({'data': data['data']})