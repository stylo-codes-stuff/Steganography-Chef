import flask
from flask import Flask, render_template, request, redirect
app = flask.Flask(__name__)

@app.route('/')
def index():
  return render_template('base.html')
if __name__ == '__main__':
  app.run(port=8080, host='0.0.0.0', debug=True)