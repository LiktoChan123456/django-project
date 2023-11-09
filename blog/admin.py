from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body')

