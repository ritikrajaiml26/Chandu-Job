from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from django import forms
from .models import Job

class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'short_description':  forms.Textarea(attrs={'rows': 5,   'class': 'vLargeTextField'}),
            'full_description':   forms.Textarea(attrs={'rows': 16,  'class': 'vLargeTextField'}),
            'eligibility':        forms.Textarea(attrs={'rows': 12,  'class': 'vLargeTextField'}),
            'important_dates':    forms.Textarea(attrs={'rows': 12,  'class': 'vLargeTextField'}),
            'selection_process':  forms.Textarea(attrs={'rows': 10,  'class': 'vLargeTextField'}),
            'how_to_apply':       forms.Textarea(attrs={'rows': 10,  'class': 'vLargeTextField'}),
        }

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobAdminForm
    list_display = ('title', 'category', 'organization_name', 'status', 'is_featured', 'is_trending', 'created_at')
    list_filter = ('status', 'is_featured', 'is_trending', 'category', 'created_at')
    search_fields = ('title', 'organization_name', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'is_featured', 'is_trending')
    readonly_fields = ('views_count',)
    
    actions = ['make_published', 'make_draft', 'toggle_featured', 'toggle_trending']


    @admin.action(description="Mark selected jobs as Published")
    def make_published(self, request, queryset):
        updated = queryset.update(status='published')
        self.message_user(
            request,
            ngettext(
                "%d job was successfully marked as published.",
                "%d jobs were successfully marked as published.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Mark selected jobs as Draft")
    def make_draft(self, request, queryset):
        updated = queryset.update(status='draft')
        self.message_user(
            request,
            ngettext(
                "%d job was successfully marked as draft.",
                "%d jobs were successfully marked as draft.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Toggle Featured status of selected jobs")
    def toggle_featured(self, request, queryset):
        for obj in queryset:
            obj.is_featured = not obj.is_featured
            obj.save()
        self.message_user(
            request,
            "Featured status toggled successfully for selected jobs.",
            messages.SUCCESS,
        )

    @admin.action(description="Toggle Trending status of selected jobs")
    def toggle_trending(self, request, queryset):
        for obj in queryset:
            obj.is_trending = not obj.is_trending
            obj.save()
        self.message_user(
            request,
            "Trending status toggled successfully for selected jobs.",
            messages.SUCCESS,
        )

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'organization_name', 'short_description', 'full_description')
        }),
        ('Job Details', {
            'fields': ('eligibility', 'age_limit', 'total_posts', 'salary', 'location')
        }),
        ('Application Details', {
            'fields': ('application_fee', 'important_dates', 'selection_process', 'how_to_apply', 'apply_link', 'official_website', 'official_notification_pdf')
        }),
        ('Media & Status', {
            'fields': ('featured_image', 'is_featured', 'is_trending', 'status', 'views_count')
        }),
    )
