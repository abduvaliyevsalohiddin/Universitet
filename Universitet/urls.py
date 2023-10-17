from django.contrib import admin
from django.urls import path
from malumot.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('hamma_yonalishlar/', hamma_yonalishlar),
    path('hamma_fanlar/', hamma_fanlar),
    path('hamma_ustozlar/', hamma_ustozlar),
]
