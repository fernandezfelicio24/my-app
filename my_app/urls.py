from django.urls import path, include
from django.contrib import admin

from .views import index, loginView, logoutView


urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
]
