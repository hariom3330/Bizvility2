from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('isAdmin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('isAdmin') is not True:
            raise ValueError('Superuser must have isAdmin=True.')

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    is_superuser = models.BooleanField(default=False)  
    isAdmin = models.BooleanField(default=False)
    contact = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    bio = models.CharField(max_length=150,default='')
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/defaultpfpsvg.png')
    forget_password_token = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        # Add this line to define permissions if needed
        permissions = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def __str__(self):
        return self.email

class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    Video = models.FileField(upload_to='video/')
    likes = models.ManyToManyField(Users, related_name='likes')
    dislikes = models.ManyToManyField(Users, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class PlanPrices(models.Model):
    PLAN_DATA_LIST = [
    ("Google business profile, Whatsapp business account, Sub domain website", "99rs"),
    ("Google business profile, Whatsapp business account, Sub domain website, Current month festive post, Managing google business page", "99rspm"),
    ("Google business profile, Whatsapp business account, Sub domain website, Current month festive post, Managing google business page, Managing social media handle's, 2 marketing post for facebook instagram and google business page, 1 cover for facebook instagram and google business page", "999rs"),
    ("Google business profile, Whatsapp business account, Sub domain website, Current month festive post, Managing google business page, Managing social media handle's, 4 marketing post for facebook instagram and google business page, 1 cover for facebook instagram and google business page, 4 social media marketing post boast on facebook or instagram", "9,999rs"),
    ("Google business profile, Whatsapp business account, Sub domain website, Current month festive post, Managing google business page, Managing social media handle's, 4 marketing post for facebook instagram and google business page, 1 cover for facebook instagram and google business page, 4 social media marketing post boast on facebook or instagram, Website static website, Domain, Hosting, Website maintenance", "14,999rs"),
    ("Google business profile, Whatsapp business account, Sub domain website, Current month festive post, Managing google business page, Managing social media handle's, 4 marketing post for facebook instagram and google business page, 1 cover for facebook instagram and google business page, 4 social media marketing post boast on facebook or instagram, Website static website, Domain, Hosting, Website maintenance, Website static website, dynamic website, Ecom, Domain, Hosting, Website maintenance, 1 time 10 product listing(in case of ecom), Billing portal, Hrm portal, Inventory portal", "19,999rs")
]
    plan_data = models.CharField(max_length=600, choices=PLAN_DATA_LIST)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Categories(models.Model):
    CATEGORY_CHOICES = [
        ('Automotive', 'Automotive'),
        ('Beauty', 'Beauty'),
        ('Hotel', 'Hotel'),
        ('Doctor', 'Doctor'),
        ('Restaurant', 'Restaurant'),
        ('Shopping', 'Shopping'),
    ]
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category


class Business(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='businesses')
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='businesses')  
    tagline = models.CharField(max_length=50, null=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='BusinessImages/')
    image1 = models.ImageField(upload_to='BusinessImages/')
    image2 = models.ImageField(upload_to='BusinessImages/')
    image3 = models.ImageField(upload_to='BusinessImages/')
    image4 = models.ImageField(upload_to='BusinessImages/')
    image5 = models.ImageField(upload_to='BusinessImages/')
    phone_number = models.CharField(max_length=13)
    website = models.URLField(max_length=200,null=True)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

    def get_google_maps_link(self):
        address_data = f"{self.address}, {self.city}, {self.state}, {self.pincode}, {self.country}"
        return f"https://www.google.com/maps/search/?api=1&query={address_data.replace(' ', '+')}"


class Restaurant(Business):
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery = models.BooleanField(default=False)
    take_out = models.BooleanField(default=False)
    AirConditioning = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    pureVeg = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    smokingAllowed = models.BooleanField(default=False)
    

class Hotel(Business):
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_service = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)


class Automotive(Business):
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    repair_services = models.BooleanField(default=False)
    parts_sales = models.BooleanField(default=False)
    towing_service = models.BooleanField(default=False)
    car_wash = models.BooleanField(default=False)
    appointment_required = models.BooleanField(default=False)


class BeautySpa(Business):
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    massage_services = models.BooleanField(default=False)
    facial_treatments = models.BooleanField(default=False)
    nail_services = models.BooleanField(default=False)
    hair_styling = models.BooleanField(default=False)
    makeup_services = models.BooleanField(default=False)
    waxing = models.BooleanField(default=False)


class Doctor(Business):
    specialty = models.CharField(max_length=255)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    accepts_insurance = models.BooleanField(default=False)
    emergency_services = models.BooleanField(default=False)
    appointment_required = models.BooleanField(default=False)


class Shopping(Business):
    clothing = models.BooleanField(default=False)
    electronics = models.BooleanField(default=False)
    groceries = models.BooleanField(default=False)
    home_goods = models.BooleanField(default=False)
    personal_care = models.BooleanField(default=False)
    discounts_available = models.BooleanField(default=False)


class BusinessHours(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, related_name='business_hours')
    mon = models.CharField(max_length=15, null=True)
    tue = models.CharField(max_length=15, null=True)
    wed = models.CharField(max_length=15, null=True)
    thu = models.CharField(max_length=15, null=True)
    fri = models.CharField(max_length=15, null=True)
    sat = models.CharField(max_length=15, null=True)
    sun = models.CharField(max_length=15, null=True)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='faqs')


class Review(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')


class SocialMedia(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='social_media')
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

