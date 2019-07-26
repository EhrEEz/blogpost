from django.contrib import admin
from post.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_date",
        "modified_date",
        "is_published",
        "creator",
        "now",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "email")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
