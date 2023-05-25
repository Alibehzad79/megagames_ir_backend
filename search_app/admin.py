from django.contrib import admin
from search_app.models import SaerchResault

# Register your models here.

@admin.register(SaerchResault)
class SaerchResaultAdmin(admin.ModelAdmin):
    list_display = ('query_name', 'research_count')
    search_fields = ("query_name",)
