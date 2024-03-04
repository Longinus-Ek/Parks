from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerCreateView, CustomerUpdateView, CustomerListView, CustomerDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/customer/', CustomerCreateView.as_view(), name='create-customer'),
    path('api/v1/customer/<int:pk>/', CustomerUpdateView.as_view(), name='create-customer'),
    path('api/v1/customer/list/', CustomerListView.as_view(), name='list-customers'),
    path('api/v1/customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete-customer'),
]
