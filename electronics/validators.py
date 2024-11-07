from rest_framework import serializers




class ArrearsValidator:
   def __init__(self, field):
       self.field = field


   def __call__(self, value):
       arrears = dict(value).get(self.field)
       if arrears:
           raise serializers.ValidationError('Запрещено обновление поля «Задолженность перед поставщиком»')