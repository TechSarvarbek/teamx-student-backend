from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['fullname',]
    list_filter = ['telegramId',]




admin.site.register(Student, StudentAdmin)
