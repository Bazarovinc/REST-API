from django.urls import path
from .views import UserView, SearchUserView

app_name = "search"

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    path('search/', SearchUserView.as_view())
]
