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
from django.contrib.auth.views import LogoutView


from .views import login_page, register_page
from events.views import EventListView, EventDetailView
from cart.views import basket, basket_update, remove_item, checkout
from addresses.views import checkout_address_create_view, checkout_address_use_view
from society.views import soc_register_page, soc_login_page
from eventmanager.views import submitEvent,event_manager_home


urlpatterns = [
    url(r'^$', login_page),
    url(r'^Events/$', EventListView, name= "Balls"),
    url(r'^Eventsmanager/$', event_manager_home, name= "eventmanager"),
    url(r'^Events/(?P<slug>[\w-]+)/$', EventDetailView, name='detail'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_use_view, name='checkout_address_use'),
    url(r'^login/$', login_page, name='login'),
    url(r'^soc_login/$', soc_login_page, name='soc_login'),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^basket/$', basket, name="basket"),
    url(r'^checkout/$', checkout, name="checkout"),
    url(r'^basket_update/$', basket_update, name="update"),
    url(r'^remove_item/$', remove_item, name="remove_item"),
    url(r'^register/$', register_page, name= "register"),
    url(r'^soc_register_page/$', soc_register_page, name= "soc_register_page"),
    url(r'^submit_event/$', submitEvent, name= "submitEvent"),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
