"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cakeshop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('cake_type/',views.cake_type),
    path('footer/', views.footer),
    path('login/', views.login),
    path('testimonial/', views.testimonial),
    path('recipe/<int:id>', views.recipe),
    path('sell_cake/',views.sell_cake),
    path('logout/', views.logout),
    path('basket/<int:id>',views.basket),
    path('remove_product/<int:id>',views.remove_product),
    path('cerousel/',views.cerousel),
    path('checkout1/',views.checkout1),
    path('checkout3/',views.checkout3),
    path('checkout4/',views.checkout4),
    path('customer_account/',views.customer_account),
    path('customer_order/',views.customer_order),
    path('customer_orders/',views.customer_orders),
    path('customer_wishlist/',views.customer_wishlist),
    path('navbar/',views.navbar),
    path('register/',views.register),
    path('about/',views.about),
    path('updateUserDetails/',views.updateUserDetails),





]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

