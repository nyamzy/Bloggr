from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment here', validators=[InputRequired()])
    submit = SubmitField('Post')

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[InputRequired()])
    content = TextAreaField('Say something', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[InputRequired()])
    submit = SubmitField('Submit')
