from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email(message='Некорректный email')])
    psw = PasswordField('Пароль: ', validators=[
        DataRequired(), Length(min=4, max=100, message='Пароль должен быть от 4 до 100 символов')]
                        )
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')
