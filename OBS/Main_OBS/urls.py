from django.urls import path
from . import views

urlpatterns = [
    path('edit_widget/', views.edit_widget, name="edit_widget"),
    path('about_widget/<slug:name_slug>/',views.ShowInfo.as_view()),
    path('edit_status/<slug:name_slug>/', views.edit_status),
    path('check_status/<slug:name_slug>/', views.CheckStatus.as_view(), name="showhide"),
    path('delete/<slug:slug_file>/', views.delete_widget, name="delete"),
    path('widget/<slug:name_slug>/', views.open_widget, name="widget"),
    path('admin_board/', views.admin_board, name="home")
]