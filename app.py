from flask import Flask
app = Flask(__name__)
#decorator-anythong before a function that starts with an @
#yatupeleka kwa broswer
@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/mombasa')
def mombasa():
	return '<h1>Hello Mombasa!</h1>'

@app.route('/town/<name>')
def town(name):
	#string formating,using f
	return f'<h1>I am in {name} </h1>'

@app.route('/town/latin/<latin_name>')
def latin(latin_name):
	latiname = ''
	if latin_name[-1] == 'y':
		latiname = latin_name[:-1] + 'iful'
	else: 
		latiname = latin_name + 'y'

	return f'<h1>My latin name is {latiname}</h1>'


if  __name__ == '__main__':
	app.run()
