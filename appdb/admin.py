from django.contrib import admin
from .models import Contact, new 

JAZZMIN_SETTINGS = {
    "site_header": "My Admin",
    "site_logo": "images/logo.png",
}
#admin.site.site_header = "TraveX"
#admin.site.site_title = "TravelX Admin Poetal"
#admin.site.index_title = "Welcome to TravelX Dashboard"
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

