from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path(r'', views.FronView.as_view(), name='FrontView'),
    path(r'<int:pk>/', views.DetailViewView.as_view(), name='DetailView'),
    path(r'listview/', views.ListViewView.as_view(), name='ListViewView'),
    path(r'createview/', views.CreateViewView.as_view(), name='CreateViewView'),
    path(r'updateview/<int:pk>', views.UpdateViewView.as_view(), name='UpdateViewView'),
    path(r'deleteview/<int:pk>', views.DeleteViewView.as_view(), name='DeleteViewView'),
    path(r'editing/<int:pk>/', views.GenericEditingView.as_view(), name='GenericEditingView'),
]
