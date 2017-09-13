"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.authtoken import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^', include('common.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=[
    url(r'^api/business/', include('Business.api_urls')),
    url(r'^api/monitor/', include('Monitor.api_urls')),
    url(r'^api/system/', include('System.api_urls')),
    url(r'^api/instantiation/', include('Instantiation.api_urls')),
    url(r'^api/host/', include('Host.api_urls')),
    url(r'^api/databases/', include('Databases.api_urls')),
]

urlpatterns+=[
    url(r'^business/', include('Business.urls')),
    url(r'^report/', include('Reports.urls')),
    url(r'^system/', include('System.urls')),
    url(r'^host/', include('Host.urls')),
    url(r'^instantiation/', include('Instantiation.urls')),
    url(r'^base/config/', include('BaseConfig.urls')),
]