import flask
from flask import Flask, request, url_for, render_template, redirect
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
    return redirect(url_for('home'))

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    # you must complete the below SQL select query
    cur.execute("SELECT idMobilityWish,studentMail,campusName FROM MobilityWish LEFT JOIN Campus ON MobilityWish.Campus_idCampus = Campus.idCampus ORDER BY idMobilityWish")
    cur2 = mysql.connection.cursor()
    # you must complete the below SQL select query
    cur2.execute("SELECT * FROM Campus ORDER BY idCampus")
    mysql.connection.commit()

    mysql.connection.commit()
    campus = cur2.fetchall()
    mobilityWish = cur.fetchall()
    return render_template('home.html', mobilityWish=mobilityWish, campus=campus)

@app.route('/add_mobility', methods=['GET'])
def add_mobility():
    cur = mysql.connection.cursor()
    # MobilityWish is the table
    # Campus_idCampus and studentMail are the fields in the table
    # SQL syntax is INSERT INTO table(field1, field2) VALUES('value1', 'value2')
    sql = "INSERT INTO MobilityWish(studentMail, Campus_idCampus) VALUES (%s, %s)"
    # request.values['choice'] and request.values['student'] are input from the form by user
    print(request.values['choice'])
    val = (request.values['student'], request.values['choice'])
    # we execute an insert query
    cur.execute(sql, val)
    # commit = save changes in database
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/edit_mobility')
def edit_mobility():
    cur = mysql.connection.cursor()

    _id = request.values['_id']
    email = request.values['email']
    _campus = request.values['campus']

    cur.execute("UPDATE MobilityWish SET studentMail=%s,Campus_idCampus=%s  WHERE idMobilityWish=%s", (email, _campus, _id))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/delete_mobility/<_id>')
def remove_mobility(_id):
    cur = mysql.connection.cursor()
    cur.execute("SET foreign_key_checks = 0;")
    cur.execute("DELETE FROM MobilityWish WHERE idMobilityWish=%s", (_id,))
    cur.execute("SET foreign_key_checks = 1;")
    mysql.connection.commit()
    return redirect(url_for('home'))





#Campus
@app.route('/campus')
def campus():
    cur = mysql.connection.cursor()
    # you must complete the below SQL select query
    cur.execute(
        "SELECT * FROM Campus ORDER BY idCampus")
    mysql.connection.commit()
    campus = cur.fetchall()

    return render_template('campus.html', campus=campus)

@app.route('/add_campus',  methods=['GET'])
def add_campus():
    cur = mysql.connection.cursor()
    # MobilityWish is the table
    # Campus_idCampus and studentMail are the fields in the table
    # SQL syntax is INSERT INTO table(field1, field2) VALUES('value1', 'value2')
    val = request.values['campus']

    cur.execute('''SELECT MAX(idCampus) FROM Campus''')
    maxid = cur.fetchone()  # (10,)
    # print(maxid)
    cur.execute('''INSERT INTO Campus(campusName, idCampus) VALUES (%s, %s)''', (val, maxid[0] + 1))
    mysql.connection.commit()
    return redirect(url_for('campus'))

@app.route('/delete_campus/<_id>')
def remove_campus(_id):
    cur = mysql.connection.cursor()
    cur.execute("SET foreign_key_checks = 0;")
    cur.execute("DELETE FROM Campus WHERE idCampus=%s", (_id,))
    cur.execute("SET foreign_key_checks = 1;")
    mysql.connection.commit()
    return redirect(url_for('campus'))

@app.route('/edit_campus')
def edit_campus():
    cur = mysql.connection.cursor()

    _id = request.values['_id']
    name = request.values['campus']

    cur.execute("UPDATE Campus SET campusName =%s WHERE idCampus=%s", (name, _id))
    mysql.connection.commit()
    return redirect(url_for('campus'))



@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/technology')
def tech():
    return render_template('tech.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7000, debug=True)
