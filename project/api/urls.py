from django.urls import path
from api import views 
urlpatterns=[
    path('',views.index.as_view(), name='index'),
]