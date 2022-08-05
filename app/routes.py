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

