from django.urls import path
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework_nested import routers
from . import views





router=routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)
router.register('carts',views.CartViewSet)
router.register('customer',views.CustomerViewSet)
router.register('order',views.OrderViewSet,basename='order')


products_router= routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product_reviews')

carts_router=routers.NestedDefaultRouter(router,'carts',lookup='cart')
carts_router.register('items',views.CartItemViewSet,basename='cart-item') # cart-item-list / cart-item-detail




# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
