from django.contrib import admin
from django.urls import path, include
from apps.usuario.api.views import Login, Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('api/', include('apps.usuario.api.routers')),
    path('api/', include('apps.modulo.routers')),
    path('api/', include('apps.dato.routers'))
]
