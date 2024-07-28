from django.contrib import admin
from .models import *
from .models import CustomUser,Listing,Video,Comments, PlanPrices

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
