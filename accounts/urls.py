from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
