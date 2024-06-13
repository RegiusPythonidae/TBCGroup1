from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, DateField, RadioField, SelectField, IntegerField, \
    SubmitField
from wtforms.validators import DataRequired, Length, equal_to
from flask_wtf.file import FileField, FileRequired


class LoginForm(FlaskForm):
    username = StringField("შეიყვანეთ იუზერნეიმი")
    password = PasswordField("შეიყვანეთ პაროლი")

    login = SubmitField("ავტორიზაცია")

class RegisterForm(FlaskForm):
    profile_image = FileField("ატვირთეთ ფაილი")
    username = StringField("შეიყვანეთ იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), Length(min=8, max=64)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(),
                                                                    equal_to("password", message="განმეორებით პაროლი და პაროლი არ ემთხვევა")])

    register = SubmitField("რეგისტრაცია")

class EditUserForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი")
    password = StringField("მომხმარებლის პაროლი")
    birthday = DateField("დაბადების თარიღი")

    save = SubmitField("ცვლილებების შენახვა")