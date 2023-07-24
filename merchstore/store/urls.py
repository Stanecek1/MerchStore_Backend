from django.urls import path
from .views import *

urlpatterns = [
    path('product_list/', ProductView.as_view(), name='product_list'),
    path('product_list/<int:pk>/', ProductDetailView.as_view(), name='product_list'),
    path('product_list_by_category/<int:category_id>/', ProductListByCategoryAPIView.as_view(),  name='product_list_by_category' ),
    path('cart/', CartRetrieveAPIView.as_view(), name='user-cart') 
]