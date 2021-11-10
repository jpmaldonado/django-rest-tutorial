from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from .views import ProductViewSet, other_view
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('other-logic/', view=other_view)

]