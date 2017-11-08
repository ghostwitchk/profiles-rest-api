from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
#things like http 404 ,http505 .these things are bieng imported.





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
