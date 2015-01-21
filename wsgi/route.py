from wsgi import app
import json

#Flask imports
from flask import render_template, session, request, redirect, url_for
import httplib2

#To use Google APIs
from apiclient.discovery import build
#Para autentificar
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/example')
def example():
  return render_template('example.html')

@app.route('/example/plots')
def plots():
  return render_template('plots.html')

@app.route('/example/maps')
def maps():
  return render_template('maps.html')

@app.route('/example/google')
def google():
  return render_template('google.html')
