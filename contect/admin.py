from django.contrib import admin
from .models import InfoID


class InfoIDAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


admin.site.register(InfoID, InfoIDAdmin)

