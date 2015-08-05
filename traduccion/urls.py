from django.conf.urls import patterns, include, url
from django.contrib import admin

from backend.views.CouponList import CouponListView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cupones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', CouponListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)