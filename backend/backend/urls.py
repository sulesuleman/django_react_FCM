from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('notify/', include('notification.urls'), name="notifications"),
    path('api-auth/', include('rest_framework.urls')),
]
