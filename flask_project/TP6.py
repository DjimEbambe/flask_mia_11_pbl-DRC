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


@app.route('/')
def index():
    # you must create a Cursor object
    # it will let you execute the needed query
    cur = mysql.connection.cursor()
    # you must complete the below SQL select query
    cur.execute("SELECT studentMail,campusName  FROM MobilityWish LEFT JOIN Campus ON MobilityWish.Campus_idCampus = Campus.idCampus")
    mysql.connection.commit()
    htmlCode = "<table border='1'>"
    htmlCode += "<tr>"  # Content the columns(Number of column)
    htmlCode += "<th>Email addresses of the students</th>"  # The first column
    htmlCode += "<th>Campuses names</th>"  # The second column
    htmlCode += "</tr>"
    # print the first cell (or column) of all rows (or records)
    for row in cur.fetchall():
        htmlCode += "<tr>"  # 1 row for all column
        htmlCode += "<td>" + str(row[0]) + "</td>"  # Row about the first column
        htmlCode += "<td>" + str(row[1]) + "</td>"  # Row about the second column
        htmlCode += "</tr>"
        cur.close()

    htmlCode += "</table>"
    return htmlCode


if __name__ == '__main__':
    app.run(debug=True)
