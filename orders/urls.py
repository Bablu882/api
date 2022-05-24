from django.urls import path
from . import views
from .views import *


urlpatterns=[
    path('hello_ord',views.HelloOrdersView.as_view(),name='hello_ord'),
    path('all',views.OrderCreateListView.as_view(),name='all'),
    path('<int:order_id>',views.OrderDetailsView.as_view(),name='order'),
    path('allofuser/<int:user_id>',views.UserOrderView.as_view(),name='viewall'),
    path('api',api_ext,name='api')
]