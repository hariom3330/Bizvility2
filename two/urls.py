
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from two.views import *
from two import views

urlpatterns = [
    path('',index,name='index'),
    path('registration/',regi,name='regi'),
    path('login/',login,name='login'),    
    path('user_logout/',user_logout, name="user_logout"),
    path('admin/',user_logout, name="user_logout"),
    path('profile/<int:user_id>',profile, name="profile"),
    path('Listing_form/',Listing_form, name="Listing_form"),
    path('select_plan/',select_plan, name="select_plan"),
    path('reels/',reels, name="reels"),  
    path('forget/',forget, name="forget"),
    path('change-password/<token>/',ChangePassword,name='change_password'),
    path('profile/update/', update_profile, name='update_profile'),
    path('result/', result, name='result'),
    path('searchByCategory/<str:category>',searchByCategory,name='searchByCategory'),
    path('listing_details/<int:listing_id>',listing_details,name='listing_details')
  
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)