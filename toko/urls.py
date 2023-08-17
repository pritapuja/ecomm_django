from django.urls import path
from . import views

app_name = 'toko'

urlpatterns = [
     path('', views.HomeListView.as_view(), name='home-produk-list'),
     path('product/<slug>/', views.ProductDetailView.as_view(), name='produk-detail'),
     path('order-summary', views.ProductDetailView.as_view(), name='order-summary-detail'),
     path('checkout/', views.CheckoutView.as_view(), name='checkout'),
     path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
     path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
     path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
     path('payment/<payment_method>', views.PaymentView.as_view(), name='payment'),
     path('paypal-return/', views.paypal_return, name='paypal-return'),
     path('paypal-cancel/', views.paypal_cancel, name='paypal-cancel'),
     path('product/', views.ObjectListView.as_view(), name='products'),
     path('tops/',views.TopstListView.as_view(), name='tops'),
     path('bottoms/',views.BottomstListView.as_view(), name='bottoms'),
     path('dresses/',views.DressListView.as_view(), name='dresses'),
     path('new/',views.NewListView.as_view(), name='new'),
     path('sale/',views.SaleListView.as_view(), name='sale'),
     path('best/',views.BestListView.as_view(), name='best'),
     path('contact/', views.ContactListView.as_view(), name="contact"),
     # path('update_item/', views.updateItem, name="update_item"),
     path('sort/', views.SortListView.as_view(), name="sort-asc"),
     path('desc/', views.DescListView.as_view(), name="sort-desc"),
     
]
