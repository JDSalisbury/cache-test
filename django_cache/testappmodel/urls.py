from .views import BlogView, BlogListView, DataBlastView, EmailView
from django.urls import path


urlpatterns = [
    path('blog/<int:pk>/', BlogView.as_view(), name="blog-get"),
    path('blogs/', BlogListView.as_view(), name="blog-all"),
    path('dataDrop/<int:pk>/', DataBlastView.as_view({'get': 'add_data'})),
    path('email/', EmailView.as_view({'get': 'email'})),

]
