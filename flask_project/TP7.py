from flask import Flask

# you should have previously installed mysql-connector
# pip install mysql-connector
from flask_mysqldb import MySQL

app = Flask(__name__)

# creates instance db of class mysql.connector
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!@10Djim'
app.config['MYSQL_DB'] = 'pblmia'
mysql = MySQL(app)


# this function is called to generate the home page of your website
@app.route('/')
def index():
    # htmlCode is some text
    htmlCode = "Hello Icam =)"
    htmlCode += "<br>"
    htmlCode += "<a href='/'>Homepage</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/list'>List</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/add'>Add</a>"
    htmlCode += "<br>"
    # this text is returned
    return htmlCode


@app.route('/list')
def list():
    # you must create a Cursor object
    # it will let you execute the needed query
    cur = mysql.connection.cursor()

    # you must complete the below SQL select query
    cur.execute("SELECT * FROM Campus ")
    mysql.connection.commit()
    htmlCode = "Menu"
    htmlCode += "<br>"
    htmlCode += "<a href='/'>Homepage</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/list'>List</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/add'>Add</a>"
    htmlCode += "<br>"
    htmlCode += "<ol>"

    # print the first cell (or column) of all rows (or records)
    for row in cur.fetchall():
        htmlCode += "<li>"
        htmlCode += str(row[1])
        htmlCode += "</li>"

    htmlCode += "</ol>"
    cur.close()
    return htmlCode


if __name__ == '__main__':
    app.run(debug=True)