from django.urls import path
from .views import UserView, SearchUserView

app_name = "search"

urlpatterns = [
    path('users/', UserView.as_view(), name='get_all_users'),
    path('users/<int:pk>', UserView.as_view(), name='get_id_user'),
    path('search/', SearchUserView.as_view(), name='get_search_users')
]
