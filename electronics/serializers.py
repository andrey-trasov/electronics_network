from rest_framework.serializers import ModelSerializer

from electronics.models import Supplier, Contacts, Products, Arrears


class SupplierSerializers(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ContactsSerializers(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class ProductsSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ArrearsSerializers(ModelSerializer):
    class Meta:
        model = Arrears
        fields = '__all__'

