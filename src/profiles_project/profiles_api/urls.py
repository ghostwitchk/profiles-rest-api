from django.conf.urls import url
from . import views


urlpatterns = [

url(r'^hello-view/' , views.HelloAPIView.as_view()),
# here when django will hello-view as the string it will call the functions or
# views of HelloAPIView (which is a class in views.py of profiles_api)
#we added as_view so that we can return the fuction as it is

]
