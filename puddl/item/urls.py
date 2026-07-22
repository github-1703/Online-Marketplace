from django.urls import path
from . import views

app_name='itemss' #app name {% url 'itemss:detail' pk=item.id %} to remove confusion
urlpatterns = [
    path('<int:pk>/',views.detail,name='detail')
]
