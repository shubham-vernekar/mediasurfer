"""MediaSurfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('api/videos/', include('videos.urls')),
    path('api/stars/', include('stars.urls')),
    path('', include('frontend.urls')),
    path('player/<id>', include('frontend.urls')),
    path('stars', include('frontend.urls')),
    path('video', include('frontend.urls')),
    path('banner', include('frontend.urls')),
    path('search', include('frontend.urls')),
    path('series', include('frontend.urls')),
    path('update', include('frontend.urls')),
    path('custom', include('frontend.urls')),
    path('login/', include('pin_passcode.urls')),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("/images/favicon.ico")),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
