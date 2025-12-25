from django.contrib import admin

# Register your models here.
from .models import Category,Blog
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('status', 'is_featured', 'category')
    search_fields = ('title', 'author__username', 'category__name')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Category)
admin.site.register(Blog)