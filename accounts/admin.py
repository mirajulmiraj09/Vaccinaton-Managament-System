from django.contrib import admin
from accounts.models import Role,User,UserRole,Profile

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','role_name')
    list_display_links = ('id','role_name')
    search_fields = ('role_name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','is_active','created_at','last_login')
    list_display_links = ('id','email')
    search_fields = ('id','email')
    list_filter = ('is_active',)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'assigned_at')
    list_display_links = ('user','role')
    list_filter = ('role',)


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'last_name', 'nid', 'phone')
#     search_fields = ('first_name', 'last_name', 'nid', 'phone')
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_email',
        'first_name',
        'last_name',
        'nid',
        'phone'
    )
    search_fields = (
        'user__id',
        'user__email',
        'first_name',
        'last_name',
        'nid',
        'phone'
    )

    def user_id(self, obj):
        return obj.user.id

    def user_email(self, obj):
        return obj.user.email

    user_id.short_description = 'User ID'
    user_email.short_description = 'Email'
