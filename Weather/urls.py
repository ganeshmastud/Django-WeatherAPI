
from django.contrib import admin
from django.urls import path
from weatherapp.views import index,delete_city
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('delete/<city_name>/',delete_city,name='delete_city')
]
