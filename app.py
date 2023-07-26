from flask import Flask, render_template
import mysql.connector as conn
db = conn.connect(host = 'localhost', user= 'root', password = '')
cursor = db.cursor()

app = Flask(__name__)


@app.route('/')
def home():
    cursor.execute("create database if not exists books")
    return "This is a page to create a Book Store"

@app.route('/add')
def addbook():
    cursor.execute("use abutalha")
    cursor.execute("select * from bank_details")
    #print(cursor.fetchall())
    return cursor.fetchall()


if __name__ == "__main__":
    app.run(debug = True)