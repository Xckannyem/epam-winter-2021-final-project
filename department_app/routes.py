from department_app import app


@app.route('/')
@app.route('/home')
def hello():
    return 'Hello, World!'


@app.route('/<string:name>')
def greeting(name):
    return f'Hello, {name}'
