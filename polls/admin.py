from django.contrib import admin
from .models import Question, Choice, Answer2, Category

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer2)
admin.site.register(Category)