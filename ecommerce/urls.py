"""ecommerce URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

#from products.views import (
#    ProductListView, 
#    product_list_view, 
#    ProductDetailView, 
#    product_detail_view, 
#    ProductFeaturedListView, 
#    ProductFeaturedDetailView,
#    ProductDetailSlugView
#)

from .views import home_page, about_page, contact_page, register_page, login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^register/$', register_page, name='register'),
    url(r'^login/$', login_page, name='login'),
    url(r'^products/', include(('products.urls', 'products'), namespace='products')),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
    url(r'^cart/', include(('carts.urls', 'cart'), namespace='cart')),


    
    
    #url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/index.html')),
    #url(r'^products/$', ProductListView.as_view()),
    #url(r'^products-fbv/$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
