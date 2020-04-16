
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

# api
import product.serializers
from rest_framework_simplejwt import views as jwt_views

# swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls' , namespace='product')),
    path('user/', include('user.urls' , namespace='user')),

    # api
    path('api-auth/', include('rest_framework.urls')),
    path('api/product/', product.serializers.ProductList.as_view()),
    path('api/product/<int:id>/', product.serializers.ProductRetrieveUpdateDestroy.as_view()),
    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('swagger/', schema_view),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)