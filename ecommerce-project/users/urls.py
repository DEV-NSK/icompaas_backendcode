from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, admin_check

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('admin-check/', admin_check, name='admin-check'),
    # path('profile/detail/', UserProfileDetailView.as_view(), name='profile-detail'),
]