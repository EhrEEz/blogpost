from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image", "total_comments", "is_published")


# class RegistrationForm(UserCreationForm):
#     class meta:
#
#         fields = ("username", "password1", "password2")


#
# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             "username",
#             "password",
#             ButtonHolder(Submit("login", "Login", css_class="btn-primary")),
#         )
#         for fieldname in ["username", "password"]:
#             self.fields[fieldname].help_text = None
