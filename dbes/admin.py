from django.contrib import admin

from . import models


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'from_email', 'creation_date', 'uuid')
    search_fields = ('recipient', 'subject', 'from_email', 'uuid')
