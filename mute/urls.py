"""mute URL Configuration

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
from muteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.UserList.as_view()),
    path('api/<id>',views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('order/',views.OrderList.as_view(),name='order'),
    path('order/<id>',views.OrderRetrieveUpdateDestroyAPIView.as_view()),
    path('category/',views.CategoryList.as_view(),name='category'),
    path('category/<id>',views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('product/',views.ProductList.as_view(),name='product'),
    path('product/<id>',views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]
