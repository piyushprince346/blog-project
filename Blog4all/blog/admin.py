from django.contrib import admin
from blog.models import Blogpost,Comment
# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Comment)