from django.conf.urls import url
from login_app import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^login/', views.login, name="login")    
]