from django.contrib import admin
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields':('first_name','last_name','username','profile_photo')
        }),
        ('Verified fields',{
            'fields':(
                'phone_number',
                'email'
            )
        }),
        ('Advanced options',{
            'fields':(
                'is_admin',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )
