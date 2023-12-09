from django.urls import path
from . import views

urlpatterns = [
    path('get-all-courses', views.CoursesListView.as_view(), name='courses-list'),
    path('get-all-lectures', views.CoursesListView.as_view(), name='lectures-list'),
]