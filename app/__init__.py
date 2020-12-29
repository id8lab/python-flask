from flask import Flask

###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'Secret Key'

from app import routes