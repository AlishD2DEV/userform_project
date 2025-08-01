from django.contrib import admin
from django.utils.html import format_html
from .models import Submission
from django.utils.safestring import mark_safe


class SubmissionAdmin(admin.ModelAdmin):
    # ✅ This method shows image previews in list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 6px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

    # ✅ Your original fields, but now image shown as preview
    list_display = ['full_name', 'email', 'address', 'image_preview', 'personal_details', 'phone', 'submitted_at']
    search_fields = ['full_name', 'email']
    ordering = ('-submitted_at', 'full_name')

    # ✅ Optional: Add filters for email domain and submission date
    list_filter = ['submitted_at']

    # ✅ Organize the fields into clean sections
    fieldsets = (
        ('Personal Info', {
            'fields': ('full_name', 'email', 'phone','personal_details')
        }),
        ('Address Details', {
            'fields': ('address',)
        }),
        ('Uploaded Image', {
            'fields': ('image',)
        }),
        ('Submitted On', {
            'fields': ('submitted_at',)
        }),
    )

admin.site.register(Submission, SubmissionAdmin)

