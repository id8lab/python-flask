from flask import Flask
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'Hello MEMpy'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)