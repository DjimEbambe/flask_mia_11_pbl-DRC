from flask import Flask

# you should have previously installed mysql-connector
# pip install mysql-connector
from flask_mysqldb import MySQL
from sshtunnel import SSHTunnelForwarder

app = Flask(__name__)

# creates instance db of class mysql.connector
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!@10Djim'
app.config['MYSQL_DB'] = 'pblmia'
mysql = MySQL(app)


@app.route('/')
def index():
    # you must create a Cursor object
    # it will let you execute the needed query
    cur = mysql.connection.cursor()
    # you must complete the below SQL select query
    cur.execute("SELECT studentMail,campusName  FROM MobilityWish LEFT JOIN Campus ON MobilityWish.Campus_idCampus = Campus.idCampus")
    mysql.connection.commit()
    htmlCode = "<ol>"

    # print the first cell (or column) of all rows (or records)
    for row in cur.fetchall():
        htmlCode += "<li>"
        htmlCode += str(row[0])
        htmlCode += "<ul>"
        htmlCode += "<li>"
        htmlCode += str(row[1])
        htmlCode += "</li>"
        htmlCode += "</ul>"
        htmlCode += "</li>"
        cur.close()
    htmlCode += "</ol>"
    return htmlCode


if __name__ == '__main__':
    app.run(debug=True)
