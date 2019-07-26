from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import PermissionDenied

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    RedirectView,
    UpdateView,
)
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, Http404

# from .forms import PostForm
from .models import Post

# from .forms import RegistrationForm
class HomePageView(TemplateView):
    template_name = "home.html"
    model = Post


class TableView(ListView):
    template_name = "table.html"
    model = Post


class BaseView(TemplateView):
    template_name = "base.html"
    model = User


class BlogListView(ListView):
    template_name = "list.html"
    model = Post


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = "post_new.html"
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = "signup.html"

    def get_success_url(self):
        messages.success(self.request, "User has been created.")
        return reverse("list")


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ("title", "description", "is_published")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=None)
        if self.request.user != obj.creator:
            raise PermissionDenied
        return obj

    def get_success_url(self):
        messages.success(self.request, f"{self.object.title} has been created.")
        return reverse("detail", args=(self.object.pk,))
