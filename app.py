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


@app.route('/')
def home():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM POSTS")
    if resultValue > 0:
        blogs = cur.fetchall()
        print(blogs)
        resValue = cur.execute("SELECT * FROM TAGSS")
        if resValue > 0:
            t = cur.fetchall()
            print(t)
            cur.close()
            return render_template('index.html', title='VOICE YOUR VIEWS', blogs=blogs, t=t)
        else:
            return render_template('index.html', title='VOICE YOUR VIEWS', blogs=blogs)
            cur.close()
    cur.close()  
    return render_template("index.html", title='VOICE YOUR VIEWS', blogs=None, t=None)



@app.route('/about')
def about():
    return render_template("about.html", title='ABOUT US')



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
        if resultValue > 0:
            user = cur.fetchone()
            if check_password_hash(user['password'], userDetails['password']):
                session['login'] = True
                session['firstName'] = user['first_name']
                session['secondName'] = user['second_name']
                flash('Welcome ' + session['firstName'] + '! You have been successfully logged in', 'success')
                mysql.connection.commit()
            else:
                cur.close()
                flash("Password does not match", 'danger')
                return render_template('login.html')
        else:
            cur.close()
            flash("Username not found", 'danger')
            return render_template('login.html')
        cur.close()
        return redirect('/')
    return render_template('login.html')



@app.route('/create', methods=['GET', 'POST'])
def create():
    session['login'] = True
    if request.method == 'POST':
        blogpost = request.form
        title = blogpost['title']
        session['title'] = title
        content = blogpost['content']
        author = session['firstName'] + " " + session['secondName']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO POSTS (title, author, content) VALUES(%s,%s,%s)", (title, author, content))
        mysql.connection.commit()
        cur.close()
        flash("Successfully posted new blog", 'success')
        return redirect('/')
    return render_template('writeblog.html')



@app.route('/tag', methods=['GET', 'POST'])
def tag():
    if request.method == 'POST':
        blogtag = request.form
        tag = blogtag['tag']
        title = blogtag['title']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT post_id FROM POSTS WHERE title = %s", [title])
        if resultValue>0:
            ind = cur.fetchone()
            print(ind['post_id'])
            cur.execute("INSERT INTO TAGSS (post_id, tag, title) VALUES (%s, %s, %s)", (ind['post_id'], tag, title))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
    return render_template('tag.html')



@app.route('/blog/<int:id>')
def blogs(id):
    session['login'] = True
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM POSTS WHERE post_id = {}".format(id))
    if resultValue > 0:
        blog = cur.fetchone()
        cur.close()
        return render_template('blog.html', blog=blog)
    return "Blog not found"



@app.route('/my-blogs', methods=['GET', 'POST'])
def my_blog():
    session['login'] = True
    author = session['firstName'] + " " + session['secondName']
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * from POSTS WHERE author = %s", [author])
    print(resultValue)
    if resultValue > 0:
        my_blogs = cur.fetchall()
        print(my_blogs)
        cur.close()
        return render_template('my-blog.html', my_blogss=my_blogs)
    else:
        cur.close()
        return render_template('my-blog.html', my_blogss=None)



@app.route('/edit-blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):
    if request.method == 'POST':
        session['login'] = True
        cur = mysql.connection.cursor()
        title = request.form['title']
        content = request.form['content']
        cur.execute("UPDATE POSTS SET title = %s, content = %s WHERE post_id = %s",(title, content, id))
        mysql.connection.commit()
        cur.close()
        flash('Blog updated successfully', 'success')
        return redirect('/blog/{}'.format(id))
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM POSTS where post_id = {}".format(id))
    if resultValue>0:
        blog = cur.fetchone()
        print(blog)
        blog_form = {}
        blog_form['title'] = blog['title']
        blog_form['content'] = blog['content']
    return render_template('editblog.html', blog_form=blog_form)



@app.route('/delete-blog/<int:id>')
def delete_blog(id):
    session['login'] = True
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM TAGSS WHERE post_id = {}".format(id))
    cur.execute("DELETE FROM POSTS WHERE post_id = {}".format(id))

    mysql.connection.commit()
    flash("Your blog has been deleted", 'success')
    return redirect('/my-blogs')



@app.route('/logout')
def logout():
    session['login'] = False
    flash("You have been logged out", 'info')
    return redirect('/login/')



@app.route('/account/delete', methods=['GET','POST'])
def account_delete():
    if request.method == 'POST':
        session['login'] = True
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
    
