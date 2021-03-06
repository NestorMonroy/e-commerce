from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from accounts.views import LoginView, RegisterView, guest_login_page
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from billing.views import payment_method_view, payment_method_createview
from marketing.views import MarketingPreferenceUpdateView
from carts.views import cart_detail_api_view
from .views import home_page, about_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^products/', include(('products.urls', 'products'), namespace='products')),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
    url(r'^cart/', include(('carts.urls', 'cart'), namespace='cart')),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view,
        name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view,
        name='checkout_address_reuse'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/guest/$', guest_login_page, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^billing/payment-method/$', payment_method_view,
        name='billing-payment-method'),
    url(r'^billing/payment-method/create/$', payment_method_createview,
        name='billing-payment-method-endpoint'),
    url(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(),
        name='marketing-pref'),




]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
