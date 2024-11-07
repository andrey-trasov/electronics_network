from django.urls import path
from rest_framework.routers import SimpleRouter

from electronics.apps import ElectronicsConfig
from electronics.views import SupplierCreateApiView, SupplierListApiView, SuppliernRetrieveAPIView, \
    SupplierUpdateAPIView, SupplierDestroyAPIView, ArrearsCreateApiView, ArrearsListApiView, ArrearsRetrieveAPIView, \
    ArrearsDestroyAPIView, ContactsViewSet, ProductsViewSet, ArrearsUpdateAPIView

app_name = ElectronicsConfig.name

#роутер
router = SimpleRouter()
router.register("contact", ContactsViewSet)
router.register("products", ProductsViewSet)

urlpatterns = [
    # Компания
    path("supplier_create/", SupplierCreateApiView.as_view(), name="supplier_create"),
    path("supplier/", SupplierListApiView.as_view(), name="supplier"),
    path("supplier/<int:pk>/", SuppliernRetrieveAPIView.as_view(), name="supplier_pk"),
    path("supplier_update/<int:pk>/", SupplierUpdateAPIView.as_view(), name="supplier_update"),
    path("supplier_delete/<int:pk>/", SupplierDestroyAPIView.as_view(), name="supplier_delete"),
    # Задолженность
    path("arrears_create/", ArrearsCreateApiView.as_view(), name="arrears_create"),
    path("arrears/", ArrearsListApiView.as_view(), name="arrears"),
    path("arrears/<int:pk>/", ArrearsRetrieveAPIView.as_view(), name="arrears_pk"),
    path("electronics_update/<int:pk>/", ArrearsUpdateAPIView.as_view(), name="electronics_update"),
    path("arrears_delete/<int:pk>/", ArrearsDestroyAPIView.as_view(), name="arrears_delete"),
]

urlpatterns += router.urls