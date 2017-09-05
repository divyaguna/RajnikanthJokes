from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^RajnikanthJokes/', include('RajnikanthJokes.urls')),
    url(r'^admin/', admin.site.urls),
]
