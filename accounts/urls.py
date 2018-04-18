from django.conf.urls import url
from . import views 
app_name = 'accounts'
urlpatterns = [
url('login/', views.login_user, name='login'), 
]