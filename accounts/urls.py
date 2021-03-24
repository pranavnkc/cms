from django.urls import path
from .views import CreateAuthor, CustomAuthToken
urlpatterns = [
    path('user/', CreateAuthor.as_view(), name="create-auther"),
    path('token/', CustomAuthToken.as_view(), name="create-auther"),
]
