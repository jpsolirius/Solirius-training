from django.contrib import admin
from blog.models import Post, Category
from projects.models import Project

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project)
# Register your models here.
