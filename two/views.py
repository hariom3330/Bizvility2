from django.contrib.auth import authenticate, login  as auth_login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from django.contrib.auth import get_user_model
from .models import CustomUser, Signup,Video
from .backends import EmailBackend 
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_mail
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from django.utils.timesince import timesince
from django.utils import timezone

def simplify_timesince(value):
    now = timezone.now()
    difference = now - value
    
    years = difference.days // 365
    months = difference.days % 365 // 30
    days = difference.days % 30
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60
    
    if years > 0:
        return f"{years} {'year' if years == 1 else 'years'} ago"
    elif months > 0:
        return f"{months} {'month' if months == 1 else 'months'} ago"
    elif days > 0:
        return f"{days} {'day' if days == 1 else 'days'} ago"
    elif hours > 0:
        return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
    elif minutes > 0:
        return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
    else:
        return f"{seconds} {'second' if seconds == 1 else 'seconds'} ago"

def index(request):
    videos = Video.objects.all()[0:4]
    return render(request,'index3.html', {'videos':videos  })

def index2(request):
    return render(request,'index.html')


def reels(request):
    videos = Video.objects.all()
    video_data = []
    for video in videos:
        video_data.append({
            'video': video,
            'likes_count': video.likes.count(),
            'dislikes_count': video.dislikes.count(),
        })

    context = {
        'videos': video_data,
    }

    if request.method == 'POST':
        action = request.headers.get('X-action')
        user = request.user
        video_id = request.POST.get('video_id')
        video = Video.objects.get(video_id=video_id)
        if action == 'like':
            if video.likes.filter(pk=user.pk).exists():
                video.likes.remove(user)
            elif not video.likes.filter(pk=user.pk).exists():
                if video.dislikes.filter(pk=user.pk).exists():
                    video.dislikes.remove(user)
                video.likes.add(user)
        elif action == 'dislike':
            if video.dislikes.filter(pk=user.pk).exists():
                video.dislikes.remove(user)
            elif not video.dislikes.filter(pk=user.pk).exists():
                if video.likes.filter(pk=user.pk).exists():
                    video.likes.remove(user)
                video.dislikes.add(user)
        elif action == 'comment':
            comment_videoID = request.POST.get('video_id')
            data = Comments.objects.filter(video=comment_videoID)
            comments_list = []
            for comment in data:
                comments_list.append({
                    'full_name': comment.user.signup.full_name,  
                    'comment': comment.comment,
                    'created_at': comment.created_at,
                    'timesince': simplify_timesince(comment.created_at)
                })
            return JsonResponse(comments_list,safe=False)
        elif action == 'add_comment':
            content = request.POST.get('comment')
            video_id = request.POST.get('video_id')

            user = request.user

            comment = Comments.objects.create(
                video_id=video_id,
                user=user,
                comment=content
            )

            commentuser = CustomUser.objects.get(id=comment.user.id)
            
            value = simplify_timesince(comment.created_at)
            if value == '0 seconds ago':
                value = 'Just now'
            return JsonResponse({
                'username': comment.user.signup.full_name,  
                'timesince': value,
                'profile': commentuser.signup.image.url if commentuser.signup.image else None   
            })
        return JsonResponse({"like":video.likes.count(),"dislike":video.dislikes.count()})
    return render(request,'reels_city.html',context)


def add(request):
    return render(request,'index4.html')
# def detail(request):
#     return render(request,'detail.html')
class ProductDetailView(View):
    def get(self,request,pk):
        listings = Listing.objects.get(id=pk)
        print(listings)
       
 

        return render(request, 'detail.html', {'Listing':listings}) 


def result(request):
    one = request.GET.get('search_value')
    all =Listing.objects.filter(name_service__icontains=one) 
    param ={'all':all}
    return render(request,'index5.html',param)  

def searchByCategory(request,category):
    all =Listing.objects.filter(category=category) 
    param ={'all':all}
    return render(request,'index5.html',param)


def Listing_form(request):
    if request.method == 'POST':
        title = request.POST.get('listing-title')
        return redirect('select_plan')
    return render(request,'Listing_form.html')

def select_plan(request):
    return render(request,'select_plan.html')

def listing(request):
    return render(request,'listing.html')

def add_listing(request):
    return render(request,'add_listing.html')
    

def regi(request):
    if request.method == "POST":
        try:
            user_type = request.POST.get('user_type')
            username = request.POST['username']
            email = request.POST['email']    
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            # # Check if username or email already exists
            # if CustomUser.objects.filter(email=email).exists():
            #     messages.info(request, 'Username already taken')
            #     return render(request, 'regi.html')
            
            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request, 'Email already taken')
                return render(request, 'regi.html')

            # Check if passwords match
            if password1 != password2:
                messages.warning(request, 'Passwords do not match. Please try again.')
                return render(request, 'regi.html')

            # Create user object
            if user_type == 'admin':
                user = CustomUser.objects.create_superuser(email=email, password=password1)
            else:
                user = CustomUser.objects.create_user(email=email, password=password1)

            # Create Signup object and associate it with the user
            signup = Signup.objects.create(user=user, full_name=username)
            signup.save()

            messages.success(request, 'Account created successfully')
            return redirect('login')  # Redirect to login page after successful registration

        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return render(request, 'regi.html')
            
    return render(request, 'regi.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # username = request.POST.get('uname')
        password = request.POST.get('password')
        user_type = request.POST.get('login_option')  # Get the selected user type

        user = authenticate(request, email=email, password=password)
        # user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if user_type == 'admin' and user.is_staff:
                    # Redirect admin users to admin panel
                    return redirect('/')
                    # return redirect('admin_panel')  # Replace 'admin_panel' with the URL name of your admin panel
                elif user_type == 'guest' and not user.is_staff:
                    # Redirect regular users to index page
                    print('User login successful')
                    return redirect('index2')  # Replace 'index' with the URL name of your index page
                else:
                    messages.error(request, "You are not authorized to access this page.")
            else:
                messages.error(request, "Your account is inactive.")
        else:
            messages.error(request, "Invalid username or password.")
    
    # Render the login page if it's a GET request or login failed
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('index')

from django.shortcuts import render, get_object_or_404
# profile
# @login_required
# def profile(request):
#     signup = Signup.objects.get(user=request.user)
#     custom_user = signup.user
#     full_name = signup.full_name
#     email = custom_user.email
    
#     return render(request, 'profile.html', {'username': full_name, 'email': email})

@login_required
def profile(request):
    user = request.user
    listings = Listing.objects.filter(user = user)
    return render(request, 'profile.html', {'user': user,'listings':listings})

from django.core.exceptions import ValidationError
import uuid
# def forget(request):
#     try:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.success(request, "Password reset instructions have been sent to your email.")
                
#                 user_obj= CustomUser.objects.get(email=email)
#                 token = str(uuid.uuid4())
#                 signup_obj=Signup.objects.get(user = user_obj)
#                 signup_obj.forget_password_token = token
#                 signup_obj.save()
#                 send_forget_password_mail(user_obj , token)
#                 message.success(request,'An email is send')
#                 return render(request,'forget.html')
#             else:
#                 messages_to_display = []
#                 for message in messages.get_messages(request):
#                     messages_to_display.append({
#                         'level': message.level,
#                         'message': message.message,
#                     })
#                 messages.error(request, "This email is not associated with any account | Register it.")
#                 return render(request,'forget.html',{'messages': messages_to_display})
#         else:
#             return render(request, 'forget.html')
#     except ValidationError as e:
#         # Handle validation errors here
#         print(f"Validation Error: {e}")
#     except Exception as e:
#         # Handle other exceptions here
#         print(f"Error: {e}")


# ************************************
# def ChangePassword(request,token):
#     context = {}

#     try:
#         signup_obj= Signup.objects.get(forget_password_token = token).first()
#         print(signup_obj)

#     except Exception as e:
#         print(e)
#     return render(request,'change-password.html')

# def forget(request):
#     try:
#         if request.method =='POST':
#             email = request.POST.get('email')

#             if not CustomUser.objects.filter(email=email).first():
#                 messages.error(request,'Not user found with  this email..')
#                 return redirect('/forget/')
#             user = CustomUser.objects.get(email= email)
#             token=str(uuid.uuid4())
#             Profile = Signup.objects.get(user = user)
#             Profile.forget_password_token = token
#             Profile.save()
            
#             send_forget_password_mail(CustomUser.email, token)
#             messages.error(request,'An Email is sent..')
#             return redirect('/forget/')
#     except Exception as e:
#         print(e)

#     return render(request , 'forget.html')

# ************************************************


def ChangePassword(request, token):
    context = {}
    try:
        signup_obj = Signup.objects.filter(forget_password_token=token)
        # Assuming you want to retrieve the associated user from Signup object
        user = signup_obj.user
        context['user'] = user
    except Signup.DoesNotExist:
        messages.error(request, 'Invalid or expired token')
        return redirect('/forget/')
    return render(request, 'change-password.html', context)

def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
   
        if not user:
            messages.error(request, 'No user found with this email')
            return redirect('/forget/')
        
        token = str(uuid.uuid4())
        profile, created = Signup.objects.get_or_create(user=user)
   
        profile.forget_password_token = token
   
        profile.save()
        send_result=send_forget_password_mail(user, token)
        if send_result:
            messages.success(request, 'An email has been sent with instructions to reset your password')
        else:
            messages.error(request, 'Failed to send reset password email. Please try again later.')
            
        # messages.success(request, 'An email has been sent with instructions to reset your password')
        return redirect('/forget/')
    return render(request, 'forget.html')

# def update_profile(request,pid):
#     data = Signup.objects.get(id=pid)
#     cat = Signup.objects.all()
#     if request.method == 'POST':
#         f = request.POST['fname']
#         l = request.POST['lname']
#         e = request.POST['email']
#         con = request.POST['contact']
#         add = request.POST['add']
#         cat = request.POST['group']
#         try:
#             im = request.FILES['image']
#             data.image=im
#             data.save()
#         except:
#             pass
#         data.user.first_name = f
#         data.user.last_name = l
#         data.user.email = e
#         data.contact = con
#         bl = Signup.objects.get(id=cat)
#         data.blood_group = bl
#         data.address = add
#         data.user.save()
#         data.save()
#         messages.success(request, "User Profile updated")
#         if request.user.is_staff:
#             return redirect('view_user')
#         else:
#             return redirect('profile')
#     d = {'data':data, 'cat':cat}
#     return render(request,'edit_profile.html',d)



@login_required
def update_profile(request):
    user = request.user
    signup_instance = Signup.objects.get(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        signup_instance.full_name = request.POST.get('full_name')
        signup_instance.contact = request.POST.get('contact')
        signup_instance.address = request.POST.get('address')
        signup_instance.dob = request.POST.get('dob')
        signup_instance.image = request.FILES.get('image')
        signup_instance.save()

        return redirect('profile')  # Redirect to profile page after successful update

    return render(request, 'update_profile.html', {'user': user, 'signup': signup_instance})
