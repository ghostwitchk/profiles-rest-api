from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""

    def create_user(self,email,name,password=None):
        """creates a new user profile object"""
        # this create_user function is pre defined function of UserProfileManager
        #and the attributes that we defined it automatically takes from the user
        #as of now i know this only(p.s confirm and change this explanantion if required)


        if not email:
            raise ValueError('user must have a email address.')
        #it raises an error if user hasnt entered his/her email

        email = self.normalize_email(email)
        #it converts all the letters in email to lower case as it is easier to
        # deal with same kind of charcters and normalize_email is function of
        # UserProfileManager and self is an object of UserProfileManager
        #and email is storing the result that it is returing

        user = self.model(email=email, name=name)
        # this 'user' is an object of UserProfile and this the way we create an
        # object for UserProfile by using self.model and then sending the
        # attributes .In this case the orange email is of UserProfile and the
        # white email is the normalised one and orange colored name is of
        #UserProfile and white name is coming from running the create_user
        # function.

        user.set_password(password)
        # it sets the password for the user in the hash form
        user.save(using=self.db)
        #it saves all the info in same database as of UserProfile


        return user

    def create_superuser(self,email,name,password):
        """"creates and saves a new superuser with given details"""

        user = self.create_user(email,name,password)
        # here user is an varaibale is different from the obove user
        #it was an object.so what we are doing here is that we are calling create_superuser
        #function inhere then passing all the agruments ann saving all the info in
        # the user

        user.is_superuser = True
        user.is_staff = True
        #these two condtions makes a user asuper user. we make these two conditions
        # true to make a user super user

        user.save(using=self.db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile"inside our system. """


    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    # the default value is true because when we wont give any or doesnt define
    # the is_active field then it will take it as true which means that person
    # active.
    is_staff = models.BooleanField(default=False)
    # here default is false because we dont want new user to be registring as
    # staff members.

    # is_active and is_staff fields are required when we substitute django user
    # model with our custom user model.

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # here we are replacing user name field with email as it is easier for
    # people to remember there email than a particular user name

    REQUIRED_FIELDS = ['name']
    # by defining fields in this we make sure that defined fields are
    #compulsary,means you can not leave these fields empty
    # we only defined name beacuse we defined email as user name fields
    # as we all know the username is a compulsary field so email automatically
    # becomes a required field


    # these are helper functions
    def get_full_name(self):
        """used to get a users full name."""
#used to get users full name .it will be used by django admin
        return self.name

    def get_short_name(self):
        """used to get a users short name."""

        return self.name


    def ___str___(self):
        """django uses this it needs to convert the object to a string"""

        return self.email
    #it is a function in which django coberts a particulat field to string so
    #it can print ,we are returing email address in this case it is unique and
    #we would like to identify a particular user by its email,so we like to
    #print a user's profile we would like to have its email printed.
