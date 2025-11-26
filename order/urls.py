from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    #payment method Start:
    #path('payment/', views.payment, name='payment'),
    #path('order_complete/', views.order_complete, name='order_complete'),
# order/urls.py তে
    path('payments/', views.payments, name='payments'),    path('order_complete/', views.order_complete, name='order_complete'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_detail/<str:order_number>/', views.order_detail, name='order_detail'),
    path('invoice/cart/', views.invoice_cart_pdf, name='invoice_cart_pdf'),
    path('invoice/download/<str:order_number>/', views.download_invoice, name='download_invoice'),  # GET (order complete পেজ থেকে)
    # urls.py 20-11-2025
    path('manage/orders/', views.manage_orders, name='manage_orders'),
    path('manage/order/<str:order_number>/', views.manage_order_edit, name='manage_order_edit'),
    path('manage/order/status-update/', views.update_order_status, name='update_order_status'),
    path('order_list/', views.order_list, name='order_list'),
    path('manage/orders/', views.manage_orders, name='manage_orders'),
    path('manage/orders/export-csv/', views.export_orders_csv, name='export_orders_csv'),
    path('manage/orders/export-excel/', views.export_orders_excel, name='export_orders_excel'),
    path('customer/summary/<int:user_id>/', views.customer_summary, name='customer_summary'),
    path('dashboard/stats/', views.dashboard_stats, name='dashboard_stats'),
    path("api/orders/", views.api_orders, name="api_orders"),
    path("api/stats/", views.api_stats, name="api_stats"),
    path('dashboard/summary/', views.dashboard_summary, name='dashboard_summary'),
    path("api/dashboard-extra/", views.api_dashboard_extra, name="api_dashboard_extra"),
    path("dashboard/", views.dashboard_page, name="dashboard"),

]
