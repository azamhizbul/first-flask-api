from flask import Flask, jsonify, request
from flask_restful import Resource

class Square(Resource):
    def get(self, num) :
        return jsonify({'square': num**2})
        