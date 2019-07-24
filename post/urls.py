from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    BaseView,
    BlogListView,
    CreatePost,
    TableView,
    PostDetail,
    SignUpView,
    UserDetail,
)
from . import views


urlpatterns = [
    path("", BlogListView.as_view(), name="list"),
    path("table/", TableView.as_view(), name="table"),
    path("post/", BlogListView.as_view(), name="list"),
    # path("create/", CreatePost.as_view(), name="create"),
    path("post/new/", CreatePost.as_view(), name="post_new"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail"),
    # path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("user/userprofile/", UserDetail.as_view(), name="user_details"),
]
