from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from flask_wtf import FlaskForm

from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить это устройство')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers, '
                                                          'dots or underscores')])
    password = PasswordField('Пароль', validators=[DataRequired(), EqualTo('password2', message='Пароли не совпадают!')])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегестрировать')

    @staticmethod
    def validate_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Этот email уже используется')

    @staticmethod
    def validate_username(field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Это имя пользователя уже используется')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль', validators=[DataRequired()])
    password = PasswordField('Новый пароль', validators=[DataRequired(),
                                                         EqualTo('password2', message='Пароли должны совпадать!')])
    password2 = PasswordField('Подтвердите новый пароль', validators=[DataRequired()])
    submit = SubmitField('Обновить пароль')


class ConfirmResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Сбросить пароль')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Новый пароль', validators=[DataRequired(),
                                                         EqualTo('password2', message='Пароли должны совпадать!')])
    password2 = PasswordField('Подтвердите новый пароль', validators=[DataRequired()])
    submit = SubmitField('Обновить пароль')


class ChangeEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Поменять почту')