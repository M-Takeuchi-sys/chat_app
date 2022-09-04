from django.urls import path, include
from rest_framework import routers

from chat_app.views import users

router = routers.DefaultRouter()
router.register('', users.UserViewSet)

urlpatterns = [
    path('', include(router.urls), name="user"),
]
