from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from electronics.models import Supplier, Contacts, Arrears, Products
from electronics.serializers import SupplierSerializers, ContactsSerializers, ArrearsSerializers, ProductsSerializers, \
    Arrears_updateSerializers


# Компания
class SupplierCreateApiView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

    def perform_create(self, serializer):
        provider = serializer.save()
        supplier = self.request.data
        #устанавливает уровень 0 если не указан поставщк
        if not "provider" in supplier or supplier == None:
            provider.level = 0
            provider.save()
        #устанавливает уровень на 1 больше чем уровень поставщика
        else:
            company = Supplier.objects.filter(id=supplier["provider"]).first()
            provider.level = company.level + 1
            provider.save()

class SupplierListApiView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

    filterset_fields = ('contacts__country',)  # фильтр


class SuppliernRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

class SupplierDestroyAPIView(DestroyAPIView):
   queryset = Supplier.objects.all()
   serializer_class = SupplierSerializers


# # Контакты компании
# class ContactsCreateApiView(CreateAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializers
#
# class ContactsListApiView(ListAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializers
#
#
# class ContactsRetrieveAPIView(RetrieveAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializers
#
#
# class ContactsUpdateAPIView(UpdateAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializers
#
# # Компания
# class SupplierCreateApiView(CreateAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializers
#
# class SupplierListApiView(ListAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializers
#
#
# class SuppliernRetrieveAPIView(RetrieveAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializers
#
#
# class SupplierUpdateAPIView(UpdateAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializers

# Задолженности
class ArrearsCreateApiView(CreateAPIView):
    queryset = Arrears.objects.all()
    serializer_class = ArrearsSerializers

class ArrearsListApiView(ListAPIView):
    queryset = Arrears.objects.all()
    serializer_class = ArrearsSerializers


class ArrearsRetrieveAPIView(RetrieveAPIView):
    queryset = Arrears.objects.all()
    serializer_class = ArrearsSerializers


class ArrearsUpdateAPIView(UpdateAPIView):
    queryset = Arrears.objects.all()
    serializer_class = Arrears_updateSerializers

class ArrearsDestroyAPIView(DestroyAPIView):
   queryset = Arrears.objects.all()
   serializer_class = ArrearsSerializers


class ContactsViewSet(ModelViewSet):
   queryset = Contacts.objects.all()
   serializer_class = ContactsSerializers

class ProductsViewSet(ModelViewSet):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializers








