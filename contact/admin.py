from django.contrib import admin
from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    # class Media:
    #     css = {
    #          'all': ('/static/admin/css/tasks.css',)
    #     }
    list_display = ['user', 'type', 'task', 'date_created', 'done']
    list_filter = ['user', 'type', 'date_created', 'done']

admin.site.register(Logo)
# admin.site.register(CreateUser)
admin.site.register(TypeTask)
admin.site.register(Task, TaskAdmin)
admin.site.register(PersonalInfo)



admin.site.site_header = 'Billing Tasks For Murodali'