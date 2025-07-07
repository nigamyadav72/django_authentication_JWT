from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id" ,"email", "name", "tc",  "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [ #yo fieldsets le garda hamro user haru lai open garda UI ja auxa athawa j j dekhauxa yesle garda dekhauxa 
        ('User Credintials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [ #while adding new user yesle tyo UI dinxa 
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "password1", "password2", "tc"],
            },
        ),
    ]
    search_fields = ["email"] #search garda email bata search garne option dinxa
    ordering = ["email", 'id']
    filter_horizontal = []


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
