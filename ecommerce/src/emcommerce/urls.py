"""emcommerce URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views


from .views import login_page, register_page, user_account, activation
from events.views import EventListView, EventDetailView
from cart.views import basket, basket_update, remove_item, checkout
from addresses.views import checkout_address_create_view, checkout_address_use_view
from society.views import soc_register_page, soc_login_page
from eventmanager.views import submitEvent,event_manager_home, complete_orders, edit_event


urlpatterns = [
    url(r'^$', login_page, name='home'),
    url(r'^Events/$', EventListView, name= "Balls"),
    url(r'^Eventsmanager/$', event_manager_home, name= "eventmanager"),
    url(r'^Events/(?P<slug>[\w-]+)/$', EventDetailView, name='detail'),
    url(r'^Orders/(?P<slug>[\w-]+)/$', complete_orders, name='complete_orders'),
    url(r'^Edit_event/(?P<slug>[\w-]+)/$', edit_event, name='edit_event'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_use_view, name='checkout_address_use'),
    url(r'^login/$', login_page, name='login'),
    url(r'^account/$', user_account, name='account'),
    url(r'^soc_login/$', soc_login_page, name='soc_login'),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^basket/$', basket, name="basket"),
    url(r'^checkout/$', checkout, name="checkout"),
    url(r'^basket_update/$', basket_update, name="update"),
    url(r'^remove_item/$', remove_item, name="remove_item"),
    url(r'^register/$', register_page, name= "register"),
    url(r'^soc_register_page/$', soc_register_page, name= "soc_register_page"),
    url(r'^submit_event/$', submitEvent, name= "submitEvent"),
    url(r'^password/change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password/change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password/reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password/reset/complete/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), url(r'^admin/', admin.site.urls),
    url(r'^activate/(?P<key>.+)$', activation),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
