from django.urls import path
from.import views


urlpatterns = [
    path('',views.sample),
    path('registration/',views.registration,name="registration/"),
    path('registration/registration',views.registration, name='registration'),
    path('login/',views.login,name='login'),
]