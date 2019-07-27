from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image", "total_comments", "is_published")


class RegisterUser(UserCreationForm):
    email = forms.EmailField(
        label=("Email address"), required=True, help_text=("Required.")
    )
    first_name = forms.CharField(label=("First Name"), max_length=50, required=True)
    last_name = forms.CharField(label=("Last Name"), max_length=50, required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user  # class RegistrationForm(UserCreationForm):


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
