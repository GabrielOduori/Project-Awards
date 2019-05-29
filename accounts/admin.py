from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
# Register your models here.


admin.site.register(Profile, ProfileAdmin)
admin.site.site_header = 'Awaards Administration'