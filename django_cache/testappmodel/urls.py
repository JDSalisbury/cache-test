from .views import BlogView, BlogListView, DataBlastView
from django.urls import path


urlpatterns = [
    path('blog/<int:pk>/', BlogView.as_view(), name="blog-get"),
    path('blogs/', BlogListView.as_view(), name="blog-all"),
    path('dataDrop/<int:pk>/', DataBlastView.as_view({'get': 'add_data'})),

]
