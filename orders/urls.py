from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order/', views.order,name='order'),
]