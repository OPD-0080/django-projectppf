from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token # for creation of token
import uuid


## choices section
ID_CARD_TYPE = (
    ("National ID", "National ID"),
    ("Voters ID", "Voters ID"),
    ("Passport ID", ("Passport ID")),
)
BUSINESS_TYPE= (
    ("Buness type 1", "Business type 1"),
    ("Buness type 2", "Business type 2"),
    ("Buness type 3", "Business type 3")
)
## ....

# Create your models here.
class APPUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email,
        first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email, password,
        first_name and last_name.
        """
        user = self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

class UserModel(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(default='', blank=True, null=True, max_length=100)
    last_name = models.CharField(default='', blank=True, null=True, max_length=100)
    middel_name = models.CharField(default='', blank=True, null=True, max_length=100)
    contact_number = models.CharField(blank=True, null=True, max_length=20)
    company = models.CharField(blank=True, null=True, max_length=20)
    department = models.CharField(blank=True, null=True, max_length=20)
    userID = models.CharField(blank=True, null=True, max_length=20)
    photo = models.CharField(blank=True, null=True, max_length=20)
    ID_card_type = models.CharField(blank=True, null=True, max_length=20, choices=ID_CARD_TYPE)
    ID_card_number = models.CharField(blank=True, null=True, max_length=20)
    ID_photo_front = models.CharField(blank=True, null=True, max_length=20)
    ID_photo_back = models.CharField(blank=True, null=True, max_length=20)
    otp = models.CharField(blank=True, null=True, max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_active_date = models.DateTimeField(blank=True, null=True)
    signup_date = models.DateTimeField(auto_now_add=True)

    objects = APPUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        is_staff = True
        return is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email
    
class RegistrationModel(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    businessName = models.CharField(default='', blank=True, null=True, max_length=100)
    natureOfBusiness = models.CharField(default='', blank=True, null=True, max_length=100)
    businessType = models.CharField(default='', blank=True, null=True, max_length=100, choices=BUSINESS_TYPE)
    location = models.CharField(default='', blank=True, null=True, max_length=100)
    address = models.CharField(default='', blank=True, null=True, max_length=100)
    contact = models.CharField(default='', blank=True, null=True, max_length=100)
    businessLogo = models.CharField(default='', blank=True, null=True, max_length=100)
    country = models.CharField(default='Ghana', blank=True, null=True, max_length=100)
    regionState = models.CharField(default='', blank=True, null=True, max_length=100)
    town = models.CharField(default='', blank=True, null=True, max_length=100)
    
    ## wrapping data in a string
    def __str__(self):
        return self.businessName
