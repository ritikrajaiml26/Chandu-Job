from django.contrib import admin
from .models import AdmitCard

@admin.register(AdmitCard)
class AdmitCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at',)
