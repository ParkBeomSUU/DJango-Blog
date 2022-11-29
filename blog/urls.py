from django.urls import path
from . import views

urlpatterns = [
 path('',views.index)
]
#''는 루트경로