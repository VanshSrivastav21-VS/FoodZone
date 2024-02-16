from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('order/', views.order, name='order'),
    path('order/confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('menu/', views.menu, name='menu'),
]