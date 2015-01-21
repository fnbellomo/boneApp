from wsgi import app
import json

# Flask imports
from flask import render_template, session, request, redirect, url_for
import httplib2

# To use Google APIs
from apiclient import discovery
# To authenticate with Google via OAuth2
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow

# Copy your credentials from the console
CLIENT_ID = "711876238709-jchulvq9841p5qiqghufp2tsd0s8bv12.apps.googleusercontent.com"
CLIENT_SECRET = 'AR-6HkfkNKujajKgujRjxnQc'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'http://a.b.com:8000/oauth2callback'

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
  if 'credentials' not in session:
    return redirect(url_for('oauth2callback'))
  credentials = client.OAuth2Credentials.from_json(session['credentials'])
  if credentials.access_token_expired:
    return redirect(url_for('oauth2callback'))
  else:
    http_auth = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v2', http_auth)
    files = drive_service.files().list().execute()
    return json.dumps(files)

@app.route('/oauth2callback')
def oauth2callback():
  flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
    client_secret = CLIENT_SECRET,
    scope = OAUTH_SCOPE,
    redirect_uri = REDIRECT_URI)
  if 'code' not in request.args:
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)
  else:
    auth_code = request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    session['credentials'] = credentials.to_json()
    return redirect(url_for('google'))

