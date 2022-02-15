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


# we use this route twice: first method to display a form
@app.route('/add')
def add():
    htmlCode = "Menu"
    htmlCode += "<br>"
    htmlCode += "<a href='/'>Homepage</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/list'>List</a>"
    htmlCode += "<br>"
    htmlCode += "<a href='/add'>Add</a>"
    htmlCode += "<br>"

    # you must create a Cursor object
    # it will let you execute the needed query
    cur = mysql.connection.cursor()

    # we look for all campuses
    cur.execute("SELECT * FROM Campus")
    mysql.connection.commit()
    htmlCode += "<br>"
    htmlCode += "Make a wish"
    htmlCode += "<br>"
    htmlCode += "<form action='addsave' method='GET''>"
    # start a form to let user enter data
    # action is the route/page called when the form is submitted
    # method indicates how the information is submitted to the other page (GET means through the URL)
    # observe the URL in your browser after submit, it will look like
    # http://127.0.0.1:5000/addsave?student=name%40icam.fr&choice=1
    # the first parameter starts with ?
    # then we have parameter1=value1
    # the second (or any subsequent parameter) starts with &
    # then we have parameter2=value2
    htmlCode += "<label>Email Address:</label>"
    htmlCode += "<br>"
    # we a have an input field of type email for the student identifier (required)
    htmlCode += "<input type='email' name='student' required>"
    htmlCode += "<br>"

    htmlCode += "<label>Campus choice:</label>"
    htmlCode += "<br>"
    # we use a drop down list to select a campus
    htmlCode += "<select name='choice'>"

    # print the first cell (or column) of all rows (or records)
    for row in cur.fetchall():
        # for each campus, we create an <option value=id>name</option>
        htmlCode += "<option value=" + str(row[0]) + ">"
        htmlCode += str(row[1])
        htmlCode += "</option>"

    # we close the select tag
    htmlCode += "</select>"

    # at the end of the form, we display a button to save the record
    htmlCode += "<br>"
    htmlCode += "<input type='submit' value='Save'>"
    # close form
    htmlCode += "</form>"
    return htmlCode

if __name__ == '__main__':
    app.run(debug=True)