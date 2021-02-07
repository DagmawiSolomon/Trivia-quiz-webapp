from django.contrib import admin
from .models import Questions, Quiz, User
# Register your models here.
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(User)