import urllib3
import flask
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
Bootstrap(app)
ckeditor = CKEditor(app)


app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

app.config['SECRET_KEY'] = 'secret'

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/')
    assert 200 == r.status

def test_about():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/about')
    assert 200 == r.status

def test_create():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/create')
    assert 200 == r.status

def test_addtag():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/tag')
    assert 200 == r.status

def test_view():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/blog/2')
    assert 200 == r.status


def test_select():
    with app.app_context():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM POSTS")
        mysql.connection.commit()
        cur.close()
    print(resultValue)
    assert 5 == resultValue


def test_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO POSTS (title, author, content) VALUES ('TESTING', 'testing', 'testing testing testing')")
        mysql.connection.commit()
        cur.execute("SELECT * FROM POSTS") #this gets record after update
        record_after = cur.fetchall()
        cur.close()
    lena = len(record_after)
    assert('testing testing testing') == record_after[lena-1]['content']
    assert('testing') == record_after[lena-1]['author']
    assert('TESTING') == record_after[lena-1]['title']

def test_update():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE POSTS SET content = 'Testing' WHERE title = 'TESTING'")
        mysql.connection.commit()
        cur.execute("SELECT * FROM POSTS")
        records_after = cur.fetchall()
        cur.close()
    lena = len(records_after)
    assert('Testing') == records_after[lena-1]['content']

def test_delete():
    with app.app_context():
        cur = mysql.connection.cursor()
        records_before = cur.execute("SELECT * FROM POSTS")
        print(records_before)
        mysql.connection.commit()
        cur.execute("DELETE FROM POSTS WHERE author = 'testing'")
        mysql.connection.commit()
        records_after = cur.execute("SELECT * FROM POSTS")
        print(records_after)
        mysql.connection.commit()
        cur.close()
    assert records_before - 1 == records_after
