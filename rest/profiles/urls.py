from django.urls import path
from .views import *

urlpatterns = [
    path("", ProfileView.as_view(), name="profile_list"),
    path("<int:pk>/", ProfileDetail.as_view(), name="profile_detial"),
    path("file/", FileView.as_view(), name="file")
    
    
]
