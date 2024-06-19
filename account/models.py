from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.

# custom user manager
class UserManager(BaseUserManager):
    def create_user(self, firstname, username, lastname, email, address, contactnumber,password=None, password2=None):
        """Creates and saves a User with the given first_name, middle_name, last_name, email, address, contact_numberand password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            firstname=firstname,
            username=username,
            lastname=lastname,
            email=self.normalize_email(email),
            address=address,
            contactnumber=contactnumber,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, username, lastname, email, address, contactnumber,password=None):
    
        user = self.create_user(
            firstname=firstname,
            username=username,
            lastname=lastname,
            email=self.normalize_email(email),
            address=address,
            contactnumber=contactnumber,
            password=password,
        )
            
        user.is_admin = True
        user.save(using=self._db)
        return user
# custom user model
class User(AbstractBaseUser):
    firstname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
    address = models.CharField(max_length=100)
    contactnumber=models.IntegerField()
    password=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'username', 'lastname', 'address', 'contactnumber']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_adminz