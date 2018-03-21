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


from .views import home_page, about_page, contact_page, login_page, register_page
from events.views import EventListView, EventDetailView
from cart.views import cart, basket_update, remove_item, checkout


urlpatterns = [
    url(r'^$', login_page),
    url(r'^about/$', about_page),
    url(r'^Events/$', EventListView, name= "Balls"),
    url(r'^Events/(?P<slug>[\w-]+)/$', EventDetailView.as_view(), name='detail'),
    url(r'^contact/$', contact_page, name= "contact"),
    url(r'^login/$', login_page),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^cart/$', cart, name="cart"),
    url(r'^checkout/$', checkout, name="checkout"),
    url(r'^basket_update/$', basket_update, name="update"),
    url(r'^remove_item/$', remove_item, name="remove_item"),
    url(r'^register/$', register_page, name= "register"),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
