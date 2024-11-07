from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("electronics/", include("electronics.urls", namespace="electronics")),
    path("user/", include("user.urls", namespace="user")),
]
