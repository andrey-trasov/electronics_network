from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
   """
   Интпоинт для регистрации пользователя
   """
   serializer_class = UserSerializer
   queryset = User.objects.all()
   permission_classes = (AllowAny,)


   def perform_create(self, serializer):
       user = serializer.save()    #не сохраняем в бд чтобы не нагружать ее
       user.set_password(user.password)    #хэшируем пароль
       user.save()