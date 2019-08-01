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

from django.views.generic.edit import CreateView, FormView, FormMixin, DeleteView
from django.http import HttpResponseRedirect, Http404

from django import forms
from ckeditor.widgets import CKEditorWidget

# from .forms import PostForm
from .models import Post, Comment
from .forms import RegisterUser, CommentForm

# from .forms import RegistrationForm
class HomePageView(TemplateView):
    template_name = "home.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_data"] = Post.objects.filter(image__isnull=False).exclude(
            image=""
        )[:5]
        return context


class TableView(ListView):
    template_name = "table.html"
    model = Post


class BaseView(TemplateView):
    template_name = "base.html"
    model = User


class BlogListView(ListView):
    template_name = "list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "Search..")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(title__contains=q)
        return queryset


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = "post_new.html"
    model = Post
    description = forms.CharField(widget=CKEditorWidget())
    fields = ("title", "description", "image", "type", "is_published")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, f"{self.object.title} has been created.")
        return reverse("list")


class PostDetail(FormMixin, DetailView):
    template_name = "details.html"
    model = Post
    form_class = CommentForm

    # For showing the comments in the the post
    def get_context_data(self, **kwargs):
        obj_post = self.get_object()
        context = super().get_context_data(**kwargs)
        # comments = Comment.objects.filter(post=obj_post)
        comments = obj_post.comment_set.all()
        context.update({"comments": comments, "total_comments": comments.count()})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        post = self.get_object()
        user = self.request.user
        form_data = form.cleaned_data
        form_data["post"] = post
        if user.is_authenticated:
            form_data["user"] = user

        Comment.objects.create(**form_data)
        return super().form_valid(form)

    def get_success_url(self):
        obj = self.get_object()
        messages.success(self.request, "Comment has been submitted")
        return reverse("detail", args=(obj.pk,))


class UserDetail(ListView):
    model = Post
    template_name = "user_details.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(creator=self.request.user)
        return queryset


class SignUpView(CreateView):
    form_class = RegisterUser
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


class CommentDelete(DeleteView):
    model = Comment

    def get_success_url(self):
        messages.success(self.request, "Comment Deleted")
        return reverse("detail", args=(self.object.post.pk,))


class PostDelete(DeleteView):
    model = Post
