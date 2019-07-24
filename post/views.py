from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    RedirectView,
)
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

# from .forms import PostForm
from .models import Post

# from .forms import RegistrationForm


class TableView(ListView):
    template_name = "table.html"
    model = Post


class BaseView(TemplateView):
    template_name = "base.html"
    model = User


class BlogListView(ListView):
    template_name = "list.html"
    model = Post


class CreatePost(CreateView):
    template_name = "post_edit.html"
    model = Post
    fields = ("title", "description", "image", "total_comments", "type", "is_published")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, f"{self.object.title} has been created.")
        return reverse("list")


class PostDetail(DetailView):
    model = Post
    template_name = "details.html"


class UserDetail(TemplateView):
    template_name = "user_details.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = "signup.html"

    def get_success_url(self):
        messages.success(self.request, "User has been created.")
        return reverse("list")


#
#
# class LoginView(FormView):
#     form_class = LoginForm
#     template_name = "login.html"
#     # success_url = "/"
#
#     def form_valid(self, form):
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         user = authenticate(username=username, password=password)
#
#         if user is not None and user.is_active:
#             login(self.request, user)
#             return super(LoginView, self).form_valid(form)
#
#         else:
#             return self.form_invalid(form)
#
#     def get_success_url(self):
#         messages.success(self.request, f"{username} has been logged in.")
#         return self.reverse("list")
#
#
# class LogOutView(RedirectView):
#
#     permanent = False
#     query_string = True
#
#     def get_redirect_url(self):
#         logout(self.request)
#         return reverse("list")


# class DeletePost(DeleteView):
#     template_name = "deletepost.html"
#     model = Post


# class LoginView(TemplateView):
#     template_name = "list.html"
#
#
# class LogOutView(TemplateView):
#     template_name = "list.html"


# class SignUpView(TemplateView):
#     template_name = "list.html"
