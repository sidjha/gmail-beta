from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
	email_data = open('testemails.json')
	emails = json.load(email_data)
	return render_template('index.html', emails=emails)

if __name__ == '__main__':
	app.debug = True
	app.run()