from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as conn
db = conn.connect(host = 'localhost', user= 'root', password = 'Abua@123')
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
    name = name.strip()
    book = Book(name,price,stock)
    msg = "Book added"
    #print(cursor.fetchall())
    return render_template("addbook.html", msg=msg)

@app.route('/bookadd')
def bookadd():
    return render_template("addbook.html") 

@app.route('/info')
def info():
    cursor.execute("create database if not exists books")
    cursor.execute("use books")
    cursor.execute("create table if not exists book1(name varchar(200), price int, stock int)")
    cursor.execute("select * from book1")
    book = cursor.fetchall()
    numbooks= len(book)
    cursor.execute("select sum(stock) from book1")
    numberofbooks = cursor.fetchall()
    return render_template('info.html', returnbooks = book,numbooks =numbooks, numberofbooks=numberofbooks)
    
    
@app.route("/delete/<i>")
def delbook(i):
    #n =  cursor.execute(f"select stock from book1 where name='{i}'")
    cursor.execute(f"delete from book1 where name='{i}'")
    #print(type(n))
    #return f"<h1>deleted book {i}</h1>"
    return redirect(url_for('info'))

@app.route('/sold/<i>')
def sold(i):
    cursor.execute(f"delete from book1 where name='{i}'")
    return redirect(url_for('info'))
    
@app.route('/sell/<i>/<s>')
def sellbook(i,s):
    ns=int(s)-1
    if ns == 0:
        cursor.execute(f"delete from book1 where name='{i}'")
        return redirect(url_for('info'))
    else:
        cursor.execute(f"update book1 set stock={ns} where name='{i}'")
        #return f'sold book {i}'    
        return redirect(url_for('info'))
    
@app.route('/add')
def firstbook():
     return render_template('addbook.html')
    
if __name__ == "__main__":
    app.run()