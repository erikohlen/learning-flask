from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField, RadioField

class SignupForm(Form):
	first_name = StringField('Org:  ')
	last_name = StringField('Var1:  ')
	twosided = StringField('Two-sided? "yes" "no":')

	submit = SubmitField('Calculate')
 