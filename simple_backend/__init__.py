from flask import Flask
import views

app = Flask(__name__)
app.config.from_object('config')
