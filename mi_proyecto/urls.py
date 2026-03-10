
from django.contrib import admin
from django.urls import include, path
from mi_aplicacion.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
]
