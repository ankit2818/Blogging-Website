from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskBlog.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min = 4, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('That Username is taken. Please choose another username.')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('That Email is taken. Please choose another email.')


class LoginForm(FlaskForm):
	# username = StringField('Username', validators = [DataRequired(), Length(min = 4, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	# confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min = 4, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	# password = PasswordField('Password', validators = [DataRequired()])
	# confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError('That Username is taken. Please choose another username.')

	def validate_email(self, email):
		if email.data != current_user.email:
			email = User.query.filter_by(email = email.data).first()
			if email:
				raise ValidationError('That Email is taken. Please choose another email.')


class RequestResetForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField("Request Password Reset")

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user is None:
			raise ValidationError('There is no account with this email. You must Register first.')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField("Reset Password")

class ChangePasswordForm(FlaskForm):
	old_password = PasswordField('Old Password', validators = [DataRequired()])
	password = PasswordField('New Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm New Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Change Password')