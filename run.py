from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/square/<int:num>', methods=['POST'])
def add(num):
	# input_json = request.get_json(force=True)
	# num1 = input_json['num1']
	# num2 = input_json['num2']
	# num1 = 5 
	# num2 = 3
	# res = num1 + num2
	res = num * num
	return {"Result": res}

@app.route('/')
def welcome():
	return "Welcome to Flask Framework"

if __name__ == "__main__":
    app.run()