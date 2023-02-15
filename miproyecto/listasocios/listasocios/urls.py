from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('socios/', include('socios.urls')),
    path('admin/', admin.site.urls),
]
