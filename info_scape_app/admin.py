from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'author')
    list_filter = ('date', 'author')
    search_fields = ('title', 'content', 'excerpt')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
