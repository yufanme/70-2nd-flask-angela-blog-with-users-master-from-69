from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("博文标题", validators=[DataRequired()])
    subtitle = StringField("副标题", validators=[DataRequired()])
    img_url = StringField("博文图片链接", validators=[DataRequired(), URL()])
    body = CKEditorField("博文内容", validators=[DataRequired()])
    submit = SubmitField("提交博文")


class RegisterForm(FlaskForm):
    email = StringField(label="邮箱", validators=[DataRequired()])
    password = PasswordField(label="密码", validators=[DataRequired()])
    name = StringField(label="昵称", validators=[DataRequired()])
    submit = SubmitField(label="注册！")


class LoginForm(FlaskForm):
    email = StringField(label="邮箱", validators=[DataRequired()])
    password = PasswordField(label="密码", validators=[DataRequired()])
    submit = SubmitField(label="登陆！")


class CommentForm(FlaskForm):
    comment = CKEditorField(label="评论", validators=[DataRequired()])
    submit = SubmitField(label="提交评论")
