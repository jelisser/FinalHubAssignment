"""finalportal URL Configuration

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
from django.contrib.auth import login
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth import views as auth_views


from nhlinfo import urls as nhlinfo_urls

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            pattern_name='calendar_urlpattern',
            permanent=False
        )),
    url(r'^calendar/$',
        TemplateView.as_view(
            template_name='nhlinfo/feeds.html'),
        name='calendar_urlpattern'
        ),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'nhlinfo/login.html'},
        name='login_urlpattern'),
    url(r'^logout/$',
        auth_views.logout,
        {'next_page':'/login/'},
        name='logout_urlpattern'),

    url(r'^admin/', admin.site.urls),
    url(r'^', include(nhlinfo_urls)),

]
