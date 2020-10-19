from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_address', 'subject', 'created_on')
    list_display_links = ('id', 'email_address')
    search_fields = ('name_first', 'name_last', 'email_address')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
