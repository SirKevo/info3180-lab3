from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '3cf8398a7a4093'
app.config['MAIL_PASSWORD'] = '9bd17c87224290'

mail = Mail(app)
from app import views