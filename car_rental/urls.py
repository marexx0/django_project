from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static  

import products
from products import views
from car_rental import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
]

if settings.DEBUG:  # Only serve media files in developmentAdd commentMore actions
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)