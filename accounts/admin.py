from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'location', 'phone', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'location')
    search_fields = ('user__username', 'user__email', 'location', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('location', 'phone',)
    ordering = ('-created_at',)

    @admin.display(description='Email')
    def email(self, obj):
        return obj.user.email
