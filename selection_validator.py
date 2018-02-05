from flask_wtf import Form
from wtforms import TextField,RadioField, SelectField,IntegerField,TextAreaField,SubmitField
from wtforms import validators, ValidationError

class ContactForm(Form):
	
	crime_type = SelectField('Crime Type', choices=[('against_women', 'Crime Against Women'), ('other', 'Other')])
	visual_type = SelectField('Visualization Type', choices=[('barchart', 'Bar Chart'), ('other', 'Other')])
	submit = SubmitField("Send")
