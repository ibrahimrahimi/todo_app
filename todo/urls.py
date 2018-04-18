from django.conf.urls import url
from . import views 

urlpatterns = [
url('index', views.index,name='index'), 
url('signup/', views.sign, name='signup'),
url('', views.home, name= 'home'),
url('addtask', views.add_task, name='add')
]