from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response




class HelloAPIView(APIView):
    """test api views."""


    def get(self, request, format=None):
        """returns a list of api views features"""


        an_apiview = ['uses http methods as functions (get,post,patch,delete)',
        'it is similar to a tradiotinal django view',
        'gives you the most control over your logic',
        'it mapped manually to urls'
        ]

        return Response({'message' : 'hello','api_view' : an_apiview})
