from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Our model register here for adminsite
from .models import Vegetable
admin.site.register(Vegetable)

#for log entry which will show us which actions are taken and when.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag']
    list_filter = ['action_flag', 'user']


# Customize the admin site header and title
admin.site.site_header = "FarmiGo"         # Title at the top of the page
admin.site.site_title = "FarmiGo Admin Portal"   # Title on the browser tab
admin.site.index_title = "Welcome to FarmiGo"  # Title on the dashboard index page

