from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validator import DataRequired, Email, TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed

class contactForm(FlaskForm):
	name = StringField ('Name', validators = [DataRequired()])
	email = StringField ('Email', validators = [DataRequired(), Email()])
	subject = StringField ('Subject', validators = [DataRequired()])
	message = StringField ('Message', validators = [DataRequired(), TextArea()])

