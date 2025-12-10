from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group

from accounts.models import Profile

class CustomAdminSite(AdminSite):
    site_header = "My Admin"

    def has_permission(self, request):
        user = request.user
        return (
            user.is_active
            and user.is_superuser
            or user.groups.filter(name="Admins").exists()
        )

custom_admin = CustomAdminSite(name="custom_admin")
custom_admin.register(User)
custom_admin.register(Group)


@admin.register(Profile, site=custom_admin)
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
