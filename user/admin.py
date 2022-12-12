from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BuiltinUserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User


class UserAdmin(BuiltinUserAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    'logo',
                    'role_id',
                    'registry_id',
                    'pointers_code',
                )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("id", "email", "first_name", "last_name")
    ordering = ('-id',)
    save_on_top = True


admin.site.register(User, UserAdmin)
