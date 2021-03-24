from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    path("", include('accounts.urls')),
    path("", include('content.urls')),
    path("token", obtain_auth_token, name='api_token_auth'),
]
