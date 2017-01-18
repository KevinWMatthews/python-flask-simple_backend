from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SOME_SETTING='default settings'
    ))
# define this environment variable to point to a settings file
app.config.from_envvar('SIMPLE_BACKEND_SETTINGS', silent=True)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
