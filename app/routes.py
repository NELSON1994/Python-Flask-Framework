from app import app


@app.route('/')
@app.route('/index')
def index():
    return "welcome to your first flask application"
