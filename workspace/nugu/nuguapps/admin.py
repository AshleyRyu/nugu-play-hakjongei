from django.contrib import admin
from .models import School
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'university', 'typical', 'start', 'end', 'term', 'first_result', 'interview_date', 'final_result']
    
admin.site.register(School, SchoolAdmin)