from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Admin view for User model"""

    list_display = ('username', 'email', 'first_name', 'last_name', 'karma', 'is_active')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'karma', 'is_active')
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'karma')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


class ProfileAdmin(admin.ModelAdmin):
    """Admin view for Profile model"""

    list_display = ('user', 'bio', 'profile_picture', 'date_of_birth', 'nationality', 'phone', 'website')
    search_fields = ('user__username', 'bio', 'nationality', 'phone', 'website')
    list_filter = ('date_of_birth', 'nationality')

    def get_queryset(self, request):
        """Optimize queryset by selecting related user"""
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user')
        return queryset

    def user(self, obj):
        return obj.user.username

    user.admin_order_field = 'user'
    user.short_description = 'Username'


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
