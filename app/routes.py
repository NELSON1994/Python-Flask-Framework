from flask import redirect, url_for, request, render_template, flash, Flask
# from werkzeug import secure_filename
from flask_mail import Mail, Message
from flask_wtf import Form
# from wtforms import *
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField, StringField
from wtforms.validators import DataRequired

import sqlite3 as sql


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nelson62moses@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.secret_key = 'development key'

from app import app

mail = Mail(app)

@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("results.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)

@app.route("/email")
def emailsending():
   msg = Message('FLASK EMAIL', sender = 'nelson62moses@gmail.com', recipients = ['nelson.otieno@andela.com'])
   msg.body = "Am sending email from flask application"
   mail.send(msg)
   return "Sent successfully"

# from config import Config

@app.route('/')
@app.route('/index')
def index():
    return "welcome to your first flask application"


@app.route('/first')
def first():
    user = {'username': 'Nelson'}
    return '''
    <html>
        <head>
            <title>Home Page - Flask App</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
            <p>Welcome onboard</p>
        </body>
    </html>'''


@app.route('/pathvariable/<name>')
def passPathVariable(name):
    # for int--> %d.  float--> %f
    return "my name is : %s" % name


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/department/<department>')
def hello_guest(department):
    return 'Department name is : %s' % department


@app.route('/department/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', department=name))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        password = request.form['password']
        print("Password is : ", password)
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        password = request.args.get('password')
        print("Password : ", password)
        return redirect(url_for('success', name=user))


@app.route('/hello/<user>/<department>/<int:marks>')
def hello_name(user, department, marks):
    return render_template('hello.html', name=user, department=department, marks=marks)


@app.route('/result')
def result():
    dictn = dict(phy=50, che=60, maths=70)
    return render_template('result.html', result=dictn)


@app.route('/loopingvalue')
def indexforlooping():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return render_template('index.html', title='Home', user=user, posts=posts)
    return render_template('body.html', title='Home', user=user, posts=posts)


@app.route('/result/formdata', methods=['POST', 'GET'])
def resultfromformtotemplate():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
    else:
        print("----> get method")


@app.route('/appkey')
def getappkey():
    print("APP KEY : ", app.config['SECRET_KEY'])
    return  '''
    <html>
        <head>
            <title>Home Page - Flask App</title>
        </head>
        <body>
            <h1>Hello, ''' + app.config['SECRET_KEY'] + '''!</h1>
            <p>Welcome onboard</p>
        </body>
    </html>'''


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        f.save(f.filename)
        return 'file uploaded successfully'


class ContactForm(Form):
    # [validators.Required("Please enter your name.")]
    # , validators.Email("Please enter your email address.")]
    name = StringField("Name Of Student", validators=[DataRequired("Please enter your name")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")
    email = StringField("Email",  validators=[DataRequired("Please enter your email")])
    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python')])
    submit = SubmitField("Send")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        # else:
        #     return render_template('success.html')
        # elif request.method == 'GET':
        # return render_template('contact.html', form=form)


@app.route('/home')
def home():
   return render_template('home.html')