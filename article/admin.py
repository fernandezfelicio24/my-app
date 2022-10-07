from django.contrib import admin

# Register your models here.
from .models import SportArticle

class SportArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'published',
        'updated',
        'slug',
    ]

admin.site.register(SportArticle, SportArticleAdmin)
