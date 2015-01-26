#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyrfc3339 import generate, parse
from datetime import datetime
import pytz

from wsgi import app
import json

# Flask imports
from flask import render_template, session, request, redirect, url_for

# To use Google APIs Client Library
from apiclient.discovery import build
# To authenticate with Google via OAuth2
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow
import httplib2



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

    files = drive_service.files().list().execute()
    #files_json = json.dumps(files, sort_keys=True, indent=4)

    result = []
    file_name = []
    file_type = []
    file_owner = []
    file_modifiedDate = []
    file_modifiedUser = []
    result.extend(files['items'])
    for item in files['items']:
      file_name.append(item['title'].encode('utf-8', 'ignore'))
      file_type.append(item['mimeType'].encode('utf-8', 'ignore'))
      file_modifiedDate.append(parse(item['modifiedDate']))
      file_modifiedUser.append(item['lastModifyingUserName'].encode('utf-8', 'ignore'))

    drive_data = [list(i) for i in zip(file_name, file_type, file_modifiedDate, file_modifiedUser)]

    return render_template('google.html', names=drive_data)

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
