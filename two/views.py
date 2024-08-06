from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
import uuid
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_mail
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


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
    return render(request, 'homePage1.html', {'videos': videos})


# def index2(request):
#     return render(request, 'index.html')


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
                    'full_name': comment.user.full_name,
                    'comment': comment.comment,
                    'created_at': comment.created_at,
                    'timesince': simplify_timesince(comment.created_at)
                })
            return JsonResponse(comments_list, safe=False)
        elif action == 'add_comment':
            content = request.POST.get('comment')
            video_id = request.POST.get('video_id')

            user = request.user

            comment = Comments.objects.create(
                video_id=video_id,
                user=user,
                comment=content
            )

            commentuser = Users.objects.get(id=comment.user.id)  # type: ignore

            value = simplify_timesince(comment.created_at)
            if value == '0 seconds ago':
                value = 'Just now'
            return JsonResponse({
                'username': comment.user.full_name,
                'timesince': value,
                'profile': commentuser.image.url if commentuser.image else None
            })
        return JsonResponse({"like": video.likes.count(), "dislike": video.dislikes.count()})
    return render(request, 'reels_city.html', context)


def add(request):
    return render(request, 'index4.html')


def result(request):
    one = request.GET.get('search_value')
    all = Business.objects.filter(title__icontains=one)
    print(one)
    param = {'listings': all, 'search_value': one}
    return render(request, 'index5.html', param)


def searchByCategory(request, category):
    listings = Business.objects.filter(category__category=category)
    print(listings)
    param = {'listings': listings, 'category': category}
    return render(request, 'searchbycategory.html', param)


def listing_details(request, listing_id):
    listing_detail = Business.objects.get(pk=listing_id)
    faqs = listing_detail.faqs.all()  # type: ignore
    context = {'listing_detail': listing_detail,
               'faqs': faqs, 'listing_id': listing_id}
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'form_a':
            user_review = request.POST.get('review')
            rating = request.POST.get('rating')
            review_data = Review.objects.create(
                user=request.user,
                rating=rating,
                comment=user_review,
                business=listing_detail
            )
        elif form_type == 'form_b':
            name = request.POST.get('name')
            print(name)
    if listing_detail.category.category == 'Restaurant':
        businessDetails = Restaurant.objects.get(title=listing_detail.title)
        context['restaurant'] = businessDetails
    elif listing_detail.category.category == 'Automotive':
        businessDetails = Automotive.objects.get(title=listing_detail.title)
        context['automotive'] = businessDetails
    elif listing_detail.category.category == 'Beauty':
        businessDetails = BeautySpa.objects.get(title=listing_detail.title)
        context['beauty_spa'] = businessDetails
    elif listing_detail.category.category == 'Hotel':
        businessDetails = Hotel.objects.get(title=listing_detail.title)
        context['hotel'] = businessDetails
    elif listing_detail.category.category == 'Doctor':
        businessDetails = Doctor.objects.get(title=listing_detail.title)
        context['doctor'] = businessDetails
    elif listing_detail.category.category == 'Shopping':
        businessDetails = Shopping.objects.get(title=listing_detail.title)
        context['shopping'] = businessDetails
    return render(request, 'listing_details.html', context)


@login_required
def Listing_form(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You are not authorized to access this page.")
    if not request.user.isAdmin:
        return HttpResponseForbidden("You are not authorized to access this page.")
    

    if request.method == 'POST':
        title = request.POST.get('title')
        tagline = request.POST.get('tagline')
        description = request.POST.get('description')
        business_category = request.POST.get('businessCategory')
        website = request.POST.get('website')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        thumbnail = request.FILES.get('thumbnail')
        images = request.FILES.getlist('images')
        print(images[3])
        return redirect('select_plan')
    return render(request, 'listing_form1.html')


def select_plan(request):
    return render(request, 'select_plan.html')


# def listing(request):
#     return render(request, 'listing.html')


# def add_listing(request):
#     return render(request, 'add_listing.html')


def regi(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        bio = request.POST.get('bio', '')
        dob = request.POST.get('dob')
        image = request.FILES['image']
        user_type = request.POST.get('user_type')
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = 'profile_images/defaultpfpsvg.png'
        if user_type == "True":
            isAdmin = True
        else:
            isAdmin = False
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
            return redirect('regi')

        user = User.objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
            contact=contact,
            address=address,
            state=state,
            city=city,
            bio=bio,
            dob=dob,
            isAdmin=isAdmin,
            image=image)  # type: ignore
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        return redirect('index')
    return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # username = request.POST.get('uname')
        password = request.POST.get('password')
        # Get the selected user type

        user = authenticate(request, email=email, password=password)
        # user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    # Render the login page if it's a GET request or login failed
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('index')


@login_required
def profile(request, user_id):
    user = request.user
    profile_user = Users.objects.get(pk=user_id)
    listings = Business.objects.filter(user=user_id)
    return render(request, 'profile.html', {'profile_user': profile_user, 'listings': listings})


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
    context = {'token':token}
    try:
        user = Users.objects.get(forget_password_token=token)
        if request.method == 'POST':
            print('Hello')
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
    except Users.DoesNotExist:
        messages.error(request, 'Invalid or expired token')
        return redirect('/forget/')
    return render(request, 'change-password.html', context)


def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Users.objects.filter(email=email).first()

        if not user:
            messages.error(request, 'No user found with this email')
            return redirect('/forget/')

        token = str(uuid.uuid4())
        profile, created = Users.objects.get_or_create(email=user)

        profile.forget_password_token = token

        profile.save()
        send_result = send_forget_password_mail(user, token)
        if send_result:
            messages.success(
                request, 'An email has been sent with instructions to reset your password')
        else:
            messages.error(
                request, 'Failed to send reset password email. Please try again later.')

        # messages.success(request, 'An email has been sent with instructions to reset your password')
        return redirect('/forget/')
    return render(request, 'forget.html')


@login_required
def update_profile(request):
    user = request.user
    signup_instance = Users.objects.get(user=user)

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

        # Redirect to profile page after successful update
        return redirect('profile')

    return render(request, 'update_profile.html', {'user': user, 'signup': signup_instance})
