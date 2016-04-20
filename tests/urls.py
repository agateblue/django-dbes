from django.conf.urls import include, url


urlpatterns = [
    url(r'^emails/', include('dbes.urls', namespace='dbes')),
]
