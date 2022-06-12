"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import re_path as url
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.views.decorators.cache import cache_page

urlpatterns = [
    # Examples
    # path('path', views.home, name='home'),
    # path('path/', include('path.urls')),

    path('admin/', admin.site.urls),
    path('', include('Application.urls')),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ url(r'^__debug__/', include(debug_toolbar.urls)),]