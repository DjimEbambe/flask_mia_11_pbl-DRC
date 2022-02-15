from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    htmlCode = "<table border='1'>"
    htmlCode += "<tr>"  # Content the columns(Number of column)
    htmlCode += "<th>title of the first column</th>"  # The first column
    htmlCode += "<th>title of the second column</th>"  # The second column
    htmlCode += "</tr>"

    for i in range(1, 5):
        htmlCode += "<tr>"  # 1 row for all column
        htmlCode += "<td>item #" + str(i) + "</td>"  # Row about the first column
        htmlCode += "<td>" + str(i * i) + "</td>"  # Row about the second column
        htmlCode += "</tr>"

    htmlCode += "</table>"

    return htmlCode


if __name__ == '__main__':
    app.run()
