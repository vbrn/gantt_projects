"""mysite URL Configuration

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
from accounts import urls as accounts_url
from home import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.HomeView.as_view(), name='home'),
    url(r'^accounts/', include(accounts_url)),
    url(r'^project/(?P<pk>\d+)/$', home_views.project_detail, name='project_detail' ),
    url(r'^send_email/(?P<pk>.+)/$', home_views.send_email, name='send_email'),
    url(r'^news/$', home_views.news, name = "news"),
    url(r'^ajax_news/$', home_views.ajax_news, name="ajax_news"),
]
