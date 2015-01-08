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
