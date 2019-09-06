
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('testappmodel.urls')),
    url(r'^admin/statuscheck/', include('celerybeat_status.urls')),

]
