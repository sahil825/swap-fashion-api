from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from django.conf.urls.static import static


urlpatterns = [
	path('admin/', admin.site.urls),
	path('v1/api/', include('api.urls')),
	path('v1/auth/', include('auth.urls')),
	path("v1/contact/", include('contactus.urls')),

]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)