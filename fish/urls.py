
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('ananas/', admin.site.urls),
    path('auth/', include('authors.urls')),
    path('', include('stikers.urls'))
]
