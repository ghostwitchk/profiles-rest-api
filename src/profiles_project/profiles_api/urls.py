from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router =  DefaultRouter()
# here we are creating an object of DefaultRouter() named router
# so that we can use all the functions of DefaultRouter class.
router.register('hello-viewset', views.HelloViewSet, base_name ='hello-viewset')
#here we are setting up different fields that are bieng required to set router
# for our viewset .'hello-viewset' is the name by which we want to call our router
# 'views.HelloViewSet' here we are registring  our view set for which
# we want to use the router.'base_name' i dont know much anything yet.

urlpatterns = [

url(r'^hello-view/' , views.HelloAPIView.as_view()),
# here when django will hello-view as the string it will call the functions or
# views of HelloAPIView (which is a class in views.py of profiles_api)
#we added as_view so that we can return the fuction as it is
url(r'', include(router.urls)),
# here we left the regular expression by doing so django will try to find the urls
# then it will go to the router.urls(P.S i'm still no clear why we did this.)
]
