from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_api.models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["contact", "name","email", "is_admin","img"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("user Credentials", {"fields": ["contact", "password"]}),
        ("Personal info", {"fields": ["name","email"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["contact","name" ,"email",'img', "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)