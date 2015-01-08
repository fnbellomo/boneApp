#!flask/bin/python
from wsgi import app
import uuid
app.secret_key = str(uuid.uuid4())
app.debug = True
app.run(host='0.0.0.0', port = 8000)
