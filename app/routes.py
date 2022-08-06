from flask import redirect, url_for, request

from app import app


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
        password= request.args.get('password')
        print("Password : ", password)
        return redirect(url_for('success', name=user))
