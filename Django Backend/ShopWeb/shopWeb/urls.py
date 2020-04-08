from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^products/$', views.ProductsView.as_view()),
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
]

