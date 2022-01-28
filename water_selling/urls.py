"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from . import views
import re

app_name = "water_selling"

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", views.logout_view, name="logout"),
    path("products/", views.products_details, name="products"),
    path("home/", views.index, name="index"),
    path("addtoCart/<int:value>/", views.addtoCart, name="addtoCart"),
    path("cart/", views.displayCart, name="cart"),
    path("emptyCart/", views.emptyCart, name="emptyCart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("checkout_success/", views.checkout_success, name="checkout_success"),
    path("place_order/", views.place_order, name="order_now"),
    path("myorders/",views.my_orders, name="my_orders"),
    path("allorders/",views.all_orders, name="all_orders"),
    path("filter_orders/",views.all_orders_filter, name="filter_orders"),
    path('accounts/', include('allauth.urls')),
]
