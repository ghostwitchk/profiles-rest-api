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
router.register('profile', views.UserProfileViewSet)
# we doont need to have a base name when we are registring a viewset for a model.
# still dont know what is the purpose of base_name
router.register('login' , views.LoginViewSet , base_name = 'login')
# we have added login api view set to our DefaultRouter
# its not a model view set so we have to set a base_name
urlpatterns = [

url(r'^hello-view/' , views.HelloAPIView.as_view()),
# here when django will hello-view as the string it will call the functions or
# views of HelloAPIView (which is a class in views.py of profiles_api)
#we added as_view so that we can return the fuction as it is
url(r'', include(router.urls)),
# here we left the regular expression by doing so django will try to find the urls
# then it will go to the router.urls .when we got to 127.0.0.1:8080/api we will
# going to find our routed url that django have created for us and the extension
# after 127.0.0.1:8080/api is the name of the router we had set.the new url will
#look something like that 127.0.0.1:8080/api/hello-viewset .you will fin things
# you will find this url on 127.0.0.1:8080/api.
]
