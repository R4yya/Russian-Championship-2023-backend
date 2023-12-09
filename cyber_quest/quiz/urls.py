from django.urls import path
from . import views

urlpatterns = [
    path('get-all-tests', views.TestsListView.as_view(), name='tests-list'),
]
