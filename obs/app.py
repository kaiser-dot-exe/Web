from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

@app.route('/')
def hello_world():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/viewAkademik')
def viewAkademik():
    con = sqlite3.connect('ogrenciler.sqlite')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT ad, soyad, fakulte, bolum FROM akademik_kadro')
    rows = cur.fetchall()
    return render_template('view.html', rows=rows)


@app.route('/viewOgrenciler')
def viewOgrenciler():
    con = sqlite3.connect('ogrenciler.sqlite')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM ogrenciler WHERE sinif=2')
    rows = cur.fetchall()
    return render_template('viewOgr.html', rows=rows)


# ZAFİYET OLAN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        numara = request.form['numara']

        con = sqlite3.connect('ogrenciler.sqlite')
        cur = con.cursor()
        query = f"SELECT * FROM ogrenciler WHERE ad = '{username}' AND numara = '{numara}'"
        cur.execute(query)
        user = cur.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('hello_world'))
        else:
            return render_template('login.html', error="Kullanıcı bulunamadı!")

    return render_template('login.html')

#
#  ZAFİYET OLMAYAN
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         numara = request.form['numara']
#
#         con = sqlite3.connect('ogrenciler.sqlite')
#         cur = con.cursor()
#         cur.execute('SELECT * FROM ogrenciler WHERE ad = ? AND numara = ?', (username, numara))
#         user = cur.fetchone()
#
#         if user:
#             session['username'] = username
#             return redirect(url_for('hello_world'))
#         else:
#             return render_template('login.html', error='Kullanıcı bulunamadı!')
#
#     return render_template('login.html')
#
#



if __name__ == '__main__':
    app.run(debug=True)
