from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, filters

from chat_app.serializers.users import UserSerializer

User = get_user_model()


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """ユーザ用APIクラス"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
