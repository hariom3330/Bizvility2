# from django.contrib.auth.models import User
# # Create your models here.
# class Signup(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     # name = models.CharField(max_length=15,unique=True)
#     email = models.CharField(max_length=50, null=True,unique=True)
#     creationdate = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.first_name
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
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    # Add this line if is_superuser is not defined in your CustomUser model
    is_superuser = models.BooleanField(default=False)

    class Meta:
        # Add this line to define permissions if needed
        permissions = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Signup(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.full_name
    

class Listing(models.Model):
    name_service = models.CharField(max_length=250)
    about_business  = models.TextField()
    Business_number =models.CharField(max_length=12)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    business_address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    business_owner_number = models.IntegerField() 
    pincode = models.IntegerField()
    main_img = models.ImageField()
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    img5 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_service 
    

class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    Video = models.FileField(upload_to='video/')
    likes = models.ManyToManyField(CustomUser,related_name='likes')
    dislikes = models.ManyToManyField(CustomUser,related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



