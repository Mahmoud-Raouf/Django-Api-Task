from django.urls import path
from . import views

 
# router = routers.DefaultRouter()
# router.register('', views_api.ProductView)

app_name= 'c'

urlpatterns = [
    # path('api/product/', include(router.urls)),
    path('', views.product_list, name='product_list'),
    path('<slug:slug>', views.product_details, name='product_detail'),


]
