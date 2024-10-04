from django.urls import path,include
from FarmiGo.rest_views.User import UserRest
from FarmiGo.rest_views.Farmer import FarmerRest


urlpatterns = [
    path("User/",UserRest.as_view()),
    path("Farmer/",FarmerRest.as_view()),
#     path("Register/",RegisterView.as_view(), name='register'),
#     path("Login/",LoginView.as_view(), name='login')
 ]