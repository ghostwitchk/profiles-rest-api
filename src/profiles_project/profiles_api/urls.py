from django.conf.urls import url
from . import views


urlpatterns = [

url(r'^hello-view/' , views.HelloAPIView.as_view()),
#we added as_view so that we can return the fuction as it is

]
