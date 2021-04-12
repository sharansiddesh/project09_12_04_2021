from django.urls import path
from app09 import views
app_name="app09"

urlpatterns = [
    path('index1/',views.index1,name="index1"),
    path('index2/<name>/',views.index2,name="index2"),
    path('index3/<gmail>/',views.index3,name="index3"),
]