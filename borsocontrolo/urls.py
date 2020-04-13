"""borsocontrolo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from companies import urls as companies_urls
from home import urls as home_urls
from negotiations import urls as negotiations_urls
from taxes import urls as taxes_urls
from investiments import urls as investiments_urls

urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('companies/', include(companies_urls)),
    path('negotiations/', include(negotiations_urls)),
    path('taxes/', include(taxes_urls)),
    path('investiments/', include(investiments_urls)),
    path('login/', LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

