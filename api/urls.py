from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('products/', view=ProductListView.as_view()),
    path('products/<int:pk>', view=ProductDetailView.as_view()),
]