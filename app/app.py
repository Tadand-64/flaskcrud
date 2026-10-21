from flask import Flask

MYSQL_HOST = 'mysql'

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"
