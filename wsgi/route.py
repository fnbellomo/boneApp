#!/usr/bin/python
# -*- coding: utf-8 -*-

from wsgi import app
import json

# Flask imports
from flask import render_template, session, request, redirect, url_for, flash

# Users data for login
from module_login.forms import MyForm
from module_login.models import DatosUsuarios

# To use Google APIs Client Library
from apiclient.discovery import build
# To authenticate with Google via OAuth2
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow
import httplib2

# To work with time of google drive file (last modifications, ....)
from pyrfc3339 import generate, parse
from datetime import datetime
import pytz


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/example/')
def example():
  return render_template('example.html')

@app.route('/example/plots/')
def plots():
  return render_template('plots.html')

@app.route('/example/maps/')
def maps():
  return render_template('maps.html')

@app.route('/example/google/')
@app.route('/example/google/<directory_id>')
def google(directory_id = None):

  # First check the credentials.
  # If no credentials are found or the credentials are invalid due to
  # expiration, new credentials need to be obtained from the authorization
  # server (the following two if).
  if 'credentials' not in session:
    return redirect(url_for('oauth2callback'))
  credentials = client.OAuth2Credentials.from_json(session['credentials'])
  if credentials.access_token_expired:
    return redirect(url_for('oauth2callback'))

  else:
    # Create an httplib2.Http object to handle our HTTP requests, and authorize it
    # using the credentials.authorize() function.
    http = httplib2.Http()
    http_auth = credentials.authorize(http)

    # The apiclient.discovery.build() function returns an instance of an API service
    # object can be used to make API calls. The object is constructed with
    # methods specific to the calendar API. The arguments provided are:
    #   name of the API ('drive')
    #   version of the API you are using ('v2')
    #   authorized httplib2.Http() object that can be used for API calls
    drive_service = build('drive', 'v2', http_auth)

    # By default, files().list() returns all files. This includes files with 
    # trashed=true. The query parameter q is to filter trashed=false.
    # For more filter parameter read
    # https://developers.google.com/drive/web/search-parameters
    param = {}
    param['q'] = 'trashed=false'
    param['maxResults'] = 1000
    files = drive_service.files().list(**param).execute()
    #files_json = json.dumps(files, sort_keys=True, indent=4)

    result = []
    result.extend(files['items'])

    # I don't know why, but some file have a empy ['parents'] parameter.
    # I don't display it's.
    b = []
    for i in range(len(result)):
      a = result[i]['parents']
      if len(a) == 0:
        b.append(i)
    for i in range(len(b)):
      result.pop(b[i] - i)    

    if directory_id == None:
      
      f = open('salida3', 'a')
      for i in range(len(result)):
        if 'headRevisionId' in result[i].keys():
          f.write('%-60s %30s %30s \n' %(result[i]['title'].encode('utf-8'), result[i]['id'].encode('utf-8'), result[i]['headRevisionId'].encode('utf-8')))
        else:
          f.write('%-60s %30s \n' %(result[i]['title'].encode('utf-8'), result[i]['id'].encode('utf-8')))
      f.close()

      select_file = []
      for i in range(len(result)):
        if result[i]['parents'][0]['isRoot'] == True:
          select_file.append(result[i])

      return render_template('google.html', all_files=select_file)

    
    elif directory_id == 'shared':

      to_show = []
      for i in range(len(result)):
        c = 0
        for j in range(len(result)):
          if result[i]['parents'][0]['id'] == result[j]['id']:
            c = c + 1
        if c == 0:
          to_show.append(result[i])
      for i in range(len(to_show)):
        if to_show[i]['shared'] == True:
          print to_show[i]['title']

      select_file = []
      for i in range(len(result)):
        if result[i]['shared'] == True:
          select_file.append(result[i])

      return render_template('google.html', all_files=select_file)


    else:
      select_file = []
      for i in range(len(result)):
        if result[i]['parents'][0]['id'] == directory_id:
          select_file.append(result[i])

      return render_template('google.html', all_files=select_file)


@app.route('/oauth2callback')
def oauth2callback():
  # Create a flow object. This object holds the client_id, client_secret, and
  # scope. It assists with OAuth 2.0 steps to get user authorization and
  # credentials.
  flow = OAuth2WebServerFlow(client_id=app.config['CLIENT_ID'],
    client_secret = app.config['CLIENT_SECRET'],
    scope = app.config['OAUTH_SCOPE'],
    redirect_uri = app.config['REDIRECT_URI'])
  if 'code' not in request.args:
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)
  else:
    auth_code = request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    session['credentials'] = credentials.to_json()
    return redirect(url_for('google'))

@app.route('/example/users/')
def usersExample():
  if "username" not in session:
    return redirect(url_for('login'))
  
  permission = []
  permission.append(session["permission"])

  return render_template("user_plots.html", permission = permission)

@app.route('/login/', methods=("GET", "POST"))
def login():
  form = MyForm()

  datos = DatosUsuarios()
  usuarios = datos.usuarios()
  permission = datos.permisos()

  if "username" in session:
    return redirect(url_for('usersExample'))

  if request.method == "POST":
    if form.validate() == True:
      session["username"] = form.username.data
        
      num_usuario = usuarios.index(form.username.data)
      session["permission"] = permission[num_usuario]
      print session["permission"]

      return redirect(url_for("usersExample"))

    if form.validate() == False:
      # If method is POST and form failed to validate
      # Do something (flash message?)
      flash('All fields are required.')
      return render_template("login.html", form=form)

  elif request.method == "GET":
    return render_template("login.html", form=form)

@app.route('/logout/')
def logout():

  if "username" not in session:
    return redirect(url_for('login'))
    
  session.pop("username", None)
  session.pop("permiso", None)
  return redirect(url_for('home'))
