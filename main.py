import flask


# Create the application.
APP = flask.Flask(name)


@APP.route('/')
def index():
    return flask.render_template('index.html')

@APP.route('/put30')
def put30():
    return flask.render_template('put.html')


if name == 'main':
    APP.debug=True
    APP.run(port=8080)