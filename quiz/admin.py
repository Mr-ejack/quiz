from django.contrib import admin

# Register your models here.

from .models import Contact, Course, Question, Result

admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)
