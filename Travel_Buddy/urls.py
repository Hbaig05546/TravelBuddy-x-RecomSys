''' /Travel_Buddy/urls.py '''

from Travel_Buddy.views import *
#from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns=[
    path('home/',home,name='home'),
    path('index/',views.IndexView.as_view(),name='index'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout),
    path('destinations/',destinationsView),
    path('profile/',profile),
    path('package_detail/',package_detail),
    path('aboutus/',aboutus),
]