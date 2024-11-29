from django.urls import path
from .views import SendFriendRequestAPIView

urlpatterns = [
path('request/<int:user_id>/', SendFriendRequestAPIView.as_view(), name='send_friendship_request'),
]