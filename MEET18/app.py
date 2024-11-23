from flask import *
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="antrian",
    password="")

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods = ["POST", "GET"] )
def simpan():
    cursor = mydb.cursor()
    id = request.form["id"]
    nama = request.form["nama"]
    nomor = request.form["nomor"]
    warna = request.form["warna"]
    query = ("insert into nomor antrian values( %s, %s, %s, %s)")
    data = ( "", nama, nomor, warna )
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect("/tampil")

@app.route('/tampil')
def tampil():
    cursor = mydb.cursor()
    cursor.execute("select * from nomor antrian")
    data = cursor.fetchall()
    return render_template('tampil.html',data=data) 

@app.route('/hapus/<id>')
def hapus(id):
    cursor = mydb.cursor()
    query = ("delete from nomor antrian where id = %s")
    data = (id,)
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<id>')
def update(id):
    cursor = mydb.cursor()
    query = ("select * from nomor antrian where id = %s")
    data = (id,)
    cursor.execute( query, data )
    value = cursor.fetchone()
    return render_template('update.html',value=value) 


@app.route('/aksiupdate', methods = ["POST", "GET"] )
def aksiupdate():
    cursor = mydb.cursor()
    id = request.form["id"]
    nama = request.form["nama"]
    nomor = request.form["nomor"]
    warna = request.form["warna"]
    query = ("insert into nomor antrian values( %s, %s, %s, %s)")
    data = ( "", nama, nomor, warna )
    cursor.execute( query, data )
    mydb.commit()
    cursor.close()
    return redirect('/tampil')

if __name__ == "__main__":
    app.run(debug=True)