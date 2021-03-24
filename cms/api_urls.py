from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", include('accounts.urls')),
    path("", include('content.urls')),
]
