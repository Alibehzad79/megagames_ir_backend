from django.contrib import admin
from settings_app.models import Setting, SocialNetwork, Contact, Ads

# Register your models here.
class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    inlines = [SocialNetworkInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'accept')
    list_editable = ('accept',)
    list_filter = ('date_sent', 'accept')
    search_fields = ('name', 'email', 'text')


admin.site.register(Ads)    