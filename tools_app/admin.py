from django.contrib import admin
from tools_app.models import Tool
# Register your models here.

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    list_editable = ("url",)
    search_fields = ("title", "url", "source")

