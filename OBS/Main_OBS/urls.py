from django.urls import path
from . import views

urlpatterns = [
    path('admin_board/', views.admin_board, name="home"),
    path('widget/<slug:name_slug>/', views.open_widget, name="widget")
]