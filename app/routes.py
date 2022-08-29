from flask import redirect, url_for, request, render_template, flash, Flask
# from werkzeug import secure_filename
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nelson62moses@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

from app import app


mail = Mail(app)

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
