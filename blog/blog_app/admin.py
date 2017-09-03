from django.contrib import admin
from blog_app.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_display_link = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
