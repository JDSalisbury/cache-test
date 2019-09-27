
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('testappmodel.urls')),
    url(r'^admin/statuscheck/', include('celerybeat_status.urls')),
    path(r'docs/', include_docs_urls(title='Cache API')),

]
