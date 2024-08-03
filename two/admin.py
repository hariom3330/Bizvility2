from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Video, Comments, PlanPrices, Categories, Business, Restaurant, Hotel, Automotive, BeautySpa, Doctor, Shopping, BusinessHours, FAQ, SocialMedia

class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ('email', 'full_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'contact', 'address', 'state', 'city', 'bio', 'dob', 'image','isAdmin')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )

    # Remove filter_horizontal attributes since they are not applicable
    filter_horizontal = ()

admin.site.register(Users, CustomUserAdmin)

admin.site.register(Video)
admin.site.register(Comments)
admin.site.register(PlanPrices)
admin.site.register(Categories)
admin.site.register(Business)
admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Automotive)
admin.site.register(BeautySpa)
admin.site.register(Doctor)
admin.site.register(Shopping)
admin.site.register(BusinessHours)
admin.site.register(FAQ)
admin.site.register(SocialMedia)
