
from flask import Flask


app = Flask(__name__)


@app.route('/welcome')
def welcome():
    msg = """
    
    <html> 
      <body> 
        <h1> Welcome </h1>
      </body>
    </html>

    """

    return msg


@app.route('/welcome/home')
def welcome_home():
    msg = """
    <html>
      <body>
        <h1> Welcome Home </h1>
      </body>
    </html>

    """
    return msg


@app.route('/welcome/back')
def welcome_back():
    msg = """
    <html>
      <body>
        <h1> Welcome Back </h1>
      </body>
    </html>

    """

    return msg

