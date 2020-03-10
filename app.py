from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
Bootstrap(app)
CKEditor(app)

app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']
mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(5)



@app.route('/')
def home():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * from POST")
    if resultValue > 0:
        blogs = cur.fetchall()
        cur.close()
        return render_template('index.html', title='REVISION BLOG', blogs=blogs)
    cur.close()
    return render_template("index.html", title='REVISION BLOG', blogs=None)



@app.route('/about')
def about():
    return render_template("about.html", title='WHAT ARE WE FOR?')



@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        if userDetails['password'] != userDetails['confirm_password']:
            flash('Password do not match! Try again.', 'danger')
            return render_template('register.html')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USER(first_name, second_name, username, email, password) VALUES (%s,%s,%s,%s,%s)", (userDetails['first_name'], userDetails['second_name'], userDetails['username'], userDetails['email'], generate_password_hash(userDetails['password'])))
        mysql.connection.commit()
        cur.close()
        flash('Registeration successful! Please login.', 'success')
        return redirect('/login/')
    return render_template('register.html')



@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM USER WHERE username = %s", ([username]))
        print(resultValue)
        if resultValue > 0:
            USER = cur.fetchall()
            info = []
            lk = []
            for row in USER:
                info.append(row)
                for i in info:
                    for j in i:
                        lk.append(j)
            print(info)
            print(lk)
            print("USER")
            print(lk[5])
            mysql.connection.commit()
            if check_password_hash(lk[5], userDetails['password']):
                print("second if")
                session['login'] = True
                session['firstName'] = lk[1]
                session['secondName'] = lk[2]
                flash('Welcome ' + session['firstName'] + '! You have been successfully logged in', 'success')
            else:
                print("second else")
                cur.close()
                flash("Password does not match", 'danger')
                return render_template('login.html')
        else:
            print("In else when result value <=0")
            cur.close()
            flash("Username not found", 'danger')
            return render_template('login.html')
        cur.close()
        return redirect('/')
    return render_template('login.html')



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        blogpost = request.form
        title = blogpost['title']
        content = blogpost['content']
        author = session.get('firstName') + ' ' + session.get('secondName')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO POST (title, author, content) VALUES(%s,%s,%s)", (title, author, content))
        mysql.connection.commit()
        cur.close()
        flash("Successfully posted new blog", 'success')
        return redirect('/')
    return render_template('writeblog.html')



@app.route('/blog/<int:id>')
def blogs(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM POST WHERE post_id = {}".format(id))
    if resultValue>0:
        blog = cur.fetchone()
        return render_template('blog.html', blog=blog)
    return "Blog not found"



@app.route('/my-blogs')
def my_blog():
    username = session['username']
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT content from POST WHERE username = %s", [username])
    if resultValue>0:
        my_blogs = cur.fetchall()
        return render_template('my-blog.html', my_blogs=my_blogs)
    else:
        return render_template('my-blog.html', my_blogs=None)



@app.route('/edit-blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        title = request.form['title']
        content = request.form['content']
        cur.execute("UPDATE Post SET title = %s, WHERE post_id = %s",(title, content, post_id))
        mysql.connection.commit()
        cur.close()
        flash('Blog updated successfully', 'success')
        return redirect('/blogs/{}'.format(id))
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Post where post_id = {}".format(id))
    if resultValue>0:
        blog = cur.fetchone()
        blog_form = {}
        blog_form['title'] = blog['title']
        blog_form['content'] = blog['content']
    return render_template('edit-blog.html', blog_form=blog_form)



@app.route('/delete-blog/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Post WHERE post_id = {}".format(id))
    mysql.connection.commit()
    flash("Your blog has been deleted", 'success')
    return redirect('/my-blogs')



@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", 'info')
    return redirect('/')



@app.route('/account/delete', methods=['GET','POST'])
def account_delete():
    if request.method == 'POST':
        userDetails = request.form
        cur = mysql.connection.cursor()
        first_name = userDetails['first_name']
        cur.execute("DELETE FROM USER WHERE first_name = %s", ([first_name]))
        mysql.connection.commit()
        cur.close()
        flash("Account deleted. Goodbye", 'danger')
        return redirect('/')
    return render_template("delete.html")



if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)


