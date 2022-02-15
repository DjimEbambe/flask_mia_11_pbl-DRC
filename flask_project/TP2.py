from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    htmlCode = "<ul>"

    for i in range(1, 5):
        htmlCode += "<li>item #" + str(i) + "</li>"

    htmlCode += "</ul>"

    return htmlCode


if __name__ == '__main__':
    app.run()
