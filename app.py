from flask import Flask, render_template, request
import mysql.connector as conn
db = conn.connect(host = 'localhost', user= 'root', password = '')
cursor = db.cursor()

app = Flask(__name__)


class Book:
    def __init__(self, name, price, stock):
        self.name= name
        self.price= price
        self.stock= stock
        cursor.execute("create database if not exists books")
        cursor.execute("use abutalha")
        cursor.execute("create table if not exists book(name varchar(20), price int, stock int)")
        cursor.execute(f"insert into book value('{self.name}', {self.price}, {self.stock})")
        
        
    def update(self,presentstock):
        self.stock = presentstock
        
@app.route('/')
def home():
   return render_template("home.html")

@app.route('/add', methods=["POST"])
def addbook():
    name = request.form["Name"]
    price = int(request.form["Price"])
    stock = int(request.form["Stock"])
    book = Book(name,price,stock)
    
    #print(cursor.fetchall())
    return "Book Added"

@app.route('/bookadd')
def bookadd():
    return render_template("addbook.html") 
    
if __name__ == "__main__":
    app.run(debug = True)