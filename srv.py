# coding: utf-8

from flask import Flask, request, render_template, Response, jsonify
import json
app = Flask(__name__)

obj = {}
store = []

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/signage")
def signage():
	return render_template("signage.html")

@app.route("/post",methods=['POST'])
def post():
	global store
	store.append(request.data.decode("utf-8"))
	
	for i in store:
		print(i)

	return Response("json")

@app.route("/get",methods=['GET'])
def get():
	global store
	tmp = []
	for i in store:
		#tmp_f = i.split(' - ')
		tmp.append(i)
	store = []
	return jsonify(tmp)

def main():
	app.run(port=5000)

if __name__ == "__main__":
	main()

	# LIFE_MAC_20のMacBook Pro