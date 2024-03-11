from django.contrib import admin
from .models import Siteuser

# Register your models here.
"""
class SiteuserAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

"""

admin.site.register(Siteuser)

