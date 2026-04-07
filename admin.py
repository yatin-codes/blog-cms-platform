from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at', 'views')
    list_filter = ('is_published', 'created_at', 'category', 'author')
    search_fields = ('title', 'content')
    
    readonly_fields = ('created_at', 'updated_at', 'views')
    
    prepopulated_fields = {'slug': ('title',)}