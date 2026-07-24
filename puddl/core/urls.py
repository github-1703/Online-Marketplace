from django.urls import path
from django.contrib.auth import views as auth_views #same views two times so as auth_views

from . import views
from .forms import LoginForm

app_name='homepage'

urlpatterns=[
    path('',views.index,name='index'),
    path('contacts/',views.contacts,name='contact_page'),
    path('signup/',views.signup,name='signup'),#signup
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',views.logout_view,name='logout'),#logout
    
] 