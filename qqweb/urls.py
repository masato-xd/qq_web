from django.conf.urls import include, url
from django.contrib import admin
from home_page import views as home_page_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'qqweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_page_views.index),
    url(r'^add/$', home_page_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', home_page_views.add2, name='add2'),
    url(r'^admin/', include(admin.site.urls)),
]
