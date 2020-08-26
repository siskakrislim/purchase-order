from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('panelwithhollow/',views.all_products,name='all-products'),
    path('accessories/',views.all_accessories,name='all-accessories'),
    path('solidpanel/',views.solid_panel,name='solid-panel'),
    path('myorders/',views.OrderedProductsByUserListView.as_view(),name='my-orders'),
    path('orderform/',views.purchase_order_form,name='purchase-order-form'),
    path('productorderform/',views.product_order_form,name='product-order-form'),

]

urlpatterns += [
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('order/create/',views.OrderCreate.as_view(),name='order_create'),
    path('order/<int:pk>/update/',views.OrderUpdate.as_view(),name='order_update'),
    path('order/<int:pk>/delete/',views.OrderDelete.as_view(),name='order_delete'),
]