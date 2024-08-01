from django.contrib import admin
from .models import *

# class SignupAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user','email')

# admin.site.register(Signup, SignupAdmin)



admin.site.register(CustomUser)


class SignupAdmin(admin.ModelAdmin):
    list_display = ['id','full_name', 'user','forget_password_token','contact','address','dob','image']

admin.site.register(Signup, SignupAdmin)
admin.site.register(Listing)

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