from flask import Flask, render_template, jsonify, redirect,url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    data = {'nama':'Udin Awaludin', 'umur':20}
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
    