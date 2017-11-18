from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# we are importing 'IsAuthenticatedOrReadOnly' package because it is an
# permission class (predefined), which only allows logged in user to do like
# status updates.
from rest_framework.permissions import IsAuthenticated
# we can use this class if we want only regustered user to see other user's
# status updates.





class HelloAPIView(APIView):

    """test api views."""

    serializer_class = serializers.HelloSerializer
    # here we are just defining or telling django about what serializer we want
    # use in ou class and serializer_class is pre defined object or somethng not sure
    # django check in serializer_class that which serializer we are using

    def get(self, request, format=None):
        """returns a list of api views features"""


        an_apiview = ['uses http methods as functions (get,post,patch,delete)',
        'it is similar to a tradiotinal django view',
        'gives you the most control over your logic',
        'it mapped manually to urls'
        ]
        # an_apiview is a list that we created.

        return Response({'message' : 'hello','api_view' : an_apiview})
# response returns our output and it always be done in the form on dictionarry
# as it had to convert whole output in jason .

    def post(self,request):
        #here response is the data tha we will send when we press the post button
        # on server
            """creates a hello mesasage with our name"""

            serializer= serializers.HelloSerializer(data=request.data)
            #in ths we created 'serializer' as an object of 'HelloSerializer class' and we store data
            #from the rquest in it
            # request.data is doing what it is taking all the data from


            if serializer.is_valid():
                a =  serializer.data.get('name')
                #THI A IS JUST A VARIABLE THAT IS BIENG USE TO RETURN THE
                #THAT WE HAVE ENTERED IN THW NEX LINE
                message = 'Hello {0}'.format(a)
                #it is a proper method of adding two strings.
                return Response({'message': message})
            else:
                return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # here we are just rasing an error if the serializer isnt valid

    def put(self,request,pk=None):
        """handles updating an object."""
# pk is the primary_key of the object that we want update but we taking this as
#none because we arnt updating any object as we dont have any object here.
# we are just creating a test function.

        return Response({'method':'put'})
    # we are doing nothing just trying to run a test function,so the things in
    #response doesnt mean anything they are there just for testing.when we actually
    # want to seriously do work then we have define the logic what we want to do.


    def patch(self,request,pk=None):
        """patch request, only updates fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """ deletes an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):

    """Test api viewsets."""
    serializer_class = serializers.HelloSerializer
    #  by doing this we tell django about the serializer

    def list(self,request):
        """returns a hello message."""

        a_viewset = [
                        'Use actions (list,create,retrive,update,partial_update)',
                       'automatically maps to URLs using routers',
                        'Provides more functionality with less code'

        ]

        return Response({'message':'HELLO!','a_viewset':a_viewset})


    def create(self,request):
        """ Creates a new hello message"""
        #exact same as the post function of apiviews
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
             a = serializer.data.get('name')
             message = 'Hello {0}'.format(a)
             return Response({'message':message})
        else:

         return Response(
         serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """handles getting an object by its ID."""
        #same as get function of api views.
        return Response({'http_method':'GET'})
    # http_method is just a key of the dictionarry and it is returing a string
    # it has no particular meaning it is a random choice of using it as a key.
    # and it is valid for all the functions down below .

    def update(self,request,pk=None):
        """handles updating an object"""

        return response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handles updating parts of an object."""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handles removing an object"""

        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating reading and updating profies."""
        #the ModelViewset class handles all the work of updating,reading and
        # deleting of profiles

    serializer_class = serializers.UserProfileSerializer
        # here we telling which serializer to use for this Class
        # and it also knows which model look for as it is defined in meta Class
        # of UserProfileSerializer
    queryset =  models.UserProfile.objects.all()
        # this queryset view set how to retrieve object from database
    authentication_classes = (TokenAuthentication,)
    # we are telling django what type of aythentication we want to use.
    # it has ',' at the end as we are creating tuple so that we can add more type
    # of authentications if we want to
    permission_classes = (permissions.UpdateOwnProfile,)
    # it also has a comma because if we want to add more permissions Class then
    # we would be able to do that it is an tuple .
    filter_backends = (filters.SearchFilter,)
    # here we are telling django whhich filter we want to use,here we are using
    # search filter.it is aslo wrriten in a tuple.
    search_fields = ('name','email',)
    # here we are defining the fields we to search by.
class LoginViewSet(viewsets.ViewSet):

    """checks email and password and returns an auth token"""
        # in this section what we are doing is that the ObtainAuthToken is an
        #APIView but we want it as a viewset.so we are returning it from a vieset
        # means at the end we will return ObtainAuthToken from a function
        # so this is how we will make it work like a viewset
    serializer_class = AuthTokenSerializer
        # we are telling django whic serailazer to use .we have imported
        #AuthTokenSerializer is a bilt in serializer it has a username field
        # and a password field that it serialzes and we have setted username as
        # email so it will make our email as a user name and password that we HAVE
        # entered to genrate a token that we have to use for authentication for other
        # apis that is why we had put the TokenAuthentication in our UserProfileViewSet
        # this whole LoginViewSet will genrate a token that it will post as we HAVE
        # returned in our create function below.

    def create(self,request):
        """usethe ObtainAuthToken APIView to validate and create a token."""
# its just a function which will return ObtainAuthToken apiview
        return ObtainAuthToken().post(request)
    # in this we are calling post function of the ObtainAuthToken api view.
    # as creation of something is related to post function.we post to create
    # something
    # now we will add this to our DefaultRouter in urls.py


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating ,reading and updating profile feed items."""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly )
    # this IsAuthenticatedOrReadOnly permission class which is predefined it
    # only allows the logged in users to do status updates or whatever they want to
    # do or it will restrict them to read only.

    def perform_create(self,serializer):
        """ sets the user profile to the logged in user"""
# it is an predefined function in ModelViewSet class that always get called
# but here we are trying to edit this as we want to set the user_profile
# to the current user .as user_profile is an foreign key we want to connect
# both the models so we are setting foreign key(user_profile) ouselves.
        serializer.save(user_profile= self.request.user)
        # we have set the user_profile to the current user
        # and we have saved it using serializer -- not sure why.
