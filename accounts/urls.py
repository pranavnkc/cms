from django.urls import path
from .views import CreateAuthor
urlpatterns = [
    path('user/', CreateAuthor.as_view(), name="create-auther"),
]
