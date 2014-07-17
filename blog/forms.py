from flask_wtf import Form
from wtforms import validators
from wtforms import TextField, TextAreaField

class PostForm(Form):
    title = TextField('Title', validators=[validators.Required()])
    content = TextAreaField('Content', validators=[validators.Required()])