# coding: utf-8

from flask import Flask, request, render_template, Response
import json
app = Flask(__name__)

store = 0

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/signage")
def signage():
	return render_template("signage.html")

@app.route("/post",methods=['POST'])
def post():
	global store
	store = request.data
	print(store) 
	return Response("json")

def main():
	app.run()

if __name__ == "__main__":
	main()