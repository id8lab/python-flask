from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

class NewsLetterForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    submit = SubmitField("Send")