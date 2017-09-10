"""ailingx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from ailingx.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),

    url(r'^home/$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),

    url(r'^usecase/$', core_views.usecase, name='usecase'),
    url(r'^feature/$', core_views.feature, name='feature'),
    url(r'^blog/$', core_views.blog, name='blog'),
    url(r'^team/$', core_views.team, name='team'),
    url(r'^joinus/$', core_views.joinus, name='joinus'),
    url(r'^contact/$', core_views.contact, name='contact'),

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
