from django.contrib import admin
from .models import Question,Choice
# Register your models here.
class Questionadmin(admin.ModelAdmin):
    list_display = ('id','pub_date','question_text')
    search_fields = ['question_text']

admin.site.register(Questionadmin,Question)
admin.site.register(Choice)