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
    LoginView,
    LogOutView,
)
from . import views


urlpatterns = [
    path("", BlogListView.as_view(), name="list"),
    path("table/", TableView.as_view(), name="table"),
    path("blog/", BlogListView.as_view(), name="list"),
    # path("create/", CreatePost.as_view(), name="create"),
    path("new/", CreatePost.as_view(), name="post_new"),
    path("blog/<int:pk>/", PostDetail.as_view(), name="detail"),
    # path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="signup"),
]
