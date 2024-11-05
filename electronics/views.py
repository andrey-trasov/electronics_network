from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from electronics.models import Supplier, Contacts, Arrears, Products
from electronics.serializers import SupplierSerializers, ContactsSerializers, ArrearsSerializers, ProductsSerializers


# Компания
class SupplierCreateApiView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

    def perform_create(self, serializer):
        level = 0
        provider = serializer.save()
        supplier = self.request.data
        print(supplier)
        if not supplier in ["provider"] and supplier != "null":
            provider.level = level
            provider.save()
        else:

            while True:
                pass


        # serializer.save()

class SupplierListApiView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


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


# class ArrearsUpdateAPIView(UpdateAPIView):
#     queryset = Arrears.objects.all()
#     serializer_class = ArrearsSerializers

class ArrearsDestroyAPIView(DestroyAPIView):
   queryset = Arrears.objects.all()
   serializer_class = ArrearsSerializers


class ContactsViewSet(ModelViewSet):
   queryset = Contacts.objects.all()
   serializer_class = ContactsSerializers

class ProductsViewSet(ModelViewSet):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializers








