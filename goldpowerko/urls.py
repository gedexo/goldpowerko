from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    [path("admin/", admin.site.urls), path("", include("web.urls", namespace="web"))]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "goldpowerko Administration"
admin.site.site_title = "goldpowerko Admin Portal"
admin.site.index_title = "Welcome to goldpowerko Admin Portal"
