from flask import Flask
import views

app = Flask(__name__)
# Read default app settings from config.py
app.config.from_object('config')
# Allow app settings to be overridden by an environment variable.
app.config.from_envvar('SIMPLE_BACKEND_SETTINGS', silent=True)
