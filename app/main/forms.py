from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[DataRequired()])
    email = StringField('Enter Your Email', validators=[DataRequired()])
    bio = TextAreaField('Tell us about you', validators=[DataRequired()])
    profile = FileField('Update Profile Picture', validators=[FileAllowed('jpg','png')])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That Email is already taken!') 

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                 raise ValidationError('That username is already taken')


class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Blog Content',validators=[DataRequired()])
    submit = SubmitField('Post')