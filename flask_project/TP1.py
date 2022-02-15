# for the complete documentation
# cf. https://flask.palletsprojects.com/en/1.1.x/quickstart/

# uses Flask library for web application development
from flask import Flask

# creates app as an instance of class Flask
# __name__ is the default application name and its value is '__main__'
app = Flask(__name__)

# def index(): defines a function index()
# @app.route('/') : associates this function to URL '/' (1st level, 1st page of your website)
# example: http://127..0.1:5000/
# this function is called to generate the home page of your website
@app.route('/')
def index():
    # htmlCode is some text
    htmlCode = "Hello Icam =) by Djim Ebambe"
    # this text is returned
    return htmlCode


if __name__ == '__main__':
    # starts the web application
    app.run()
