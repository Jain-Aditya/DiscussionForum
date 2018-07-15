from django.contrib import admin
from .models import Category,Discussion,Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Discussion)
admin.site.register(Comment)