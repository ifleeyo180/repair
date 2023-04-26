from django.contrib import admin
from .models import Tag, TagManagement
# Register your models here.
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(TagManagement, admin.ModelAdmin)

