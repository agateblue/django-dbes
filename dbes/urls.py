from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<uuid>[-\w]+)$', views.EmailDetail.as_view(), name="email-detail"),
]
