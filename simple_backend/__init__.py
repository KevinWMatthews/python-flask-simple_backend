from flask import Flask

app = Flask(__name__)
# Read default app settings from config.py
app.config.from_object('config')
# Allow app settings to be overridden by an environment variable.
app.config.from_envvar('SIMPLE_BACKEND_SETTINGS', silent=True)

# Import all pages *after* the app is created.
from views.index import index_page
from views.upload import upload_page

# Register all pages with blueprint.
app.register_blueprint(index_page)
app.register_blueprint(upload_page)
