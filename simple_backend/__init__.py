from flask import Flask

app = Flask(__name__)
# Read default app settings from config.py
app.config.from_object('config')
# Allow app settings to be overridden by an environment variable.
app.config.from_envvar('SIMPLE_BACKEND_SETTINGS', silent=True)

# Import all pages *after* the app is created.
# I've rigged up this view (default.py) to render html files be default.
from views.default import default_view
# If you need to do something special, create and import a custom view.
from views.upload import upload_view
from views.data_url import data_url_view

# Register all pages with blueprint.
app.register_blueprint(default_view)
app.register_blueprint(upload_view)
app.register_blueprint(data_url_view)
