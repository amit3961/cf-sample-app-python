# import dependencies
import os
from flask import Flask

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 5000 for local development
port = int(os.getenv('PORT', '5000'))

# our base route which just returns a string
@app.route('/hello_world')
def hello_world():
    return 'Congratulations! Welcome to the Swisscom Application Cloud.'

# start the app
if __name__ == '__main__':
    app.run(host='10.0.1.4')
