from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.uplpoad_image),
    path('success/', views.success, name="success"),
    path('edit/<str:pk>', views.edit_image, name="edit"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
