from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser





class UserManager(BaseUserManager):
    def create_user(self, contact,name, email, password=None,password2=None):
        """
        Creates and saves a User with the given email, contact,name and password.
        """
        if not contact:
            raise ValueError("Users must have an email address")

        user = self.model(
            contact=contact,
            name=name,
            email=self.normalize_email(email)
           
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, contact, name, email, password=None):
        """
        Creates and saves a superuser with the given contact,name, email, and password.
        """
        user = self.create_user(
            contact,
            name,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    contact=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    img=models.ImageField(upload_to='pics')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "contact"
    REQUIRED_FIELDS = ["name","email"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin