from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from import_export.admin import ImportExportActionModelAdmin

class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id', 'name')


admin.site.register(Contact, ContactAdmin)
