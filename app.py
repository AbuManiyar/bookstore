from flask import Flask, render_template, request
import mysql.connector as conn
db = conn.connect(host = 'localhost', user= 'root', password = '@123')
cursor = db.cursor()
app = Flask(__name__)


class Book:
    def __init__(self, name, price, stock):
        self.name= name
        self.price= price
        self.stock= stock
        cursor.execute(f"insert into book1 value('{self.name}', {self.price}, {self.stock})")
        
        
    def update(self,presentstock):
        self.stock = presentstock
        
@app.route('/')
def home():
    cursor.execute("create database if not exists books")
    cursor.execute("use books")
    cursor.execute("create table if not exists book1(name varchar(200), price int, stock int)")
    return render_template("home.html")

@app.route('/add', methods=["POST"])
def addbook():
    name = request.form["Name"]
    price = int(request.form["Price"])
    stock = int(request.form["Stock"])
    book = Book(name,price,stock)
    
    #print(cursor.fetchall())
    return "<h1>Book Added</h1>"

@app.route('/bookadd')
def bookadd():
    return render_template("addbook.html") 

@app.route('/info')
def info():
    cursor.execute("select * from book1")
    book = cursor.fetchall()
    return render_template('info.html', returnbooks = book )
    
if __name__ == "__main__":
    app.run()