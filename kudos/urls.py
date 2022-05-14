from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings
from app import views
from app.views import MyInfo


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'users-available', views.UsersAvailableViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'kudos-sent', views.KudoSentViewSet)
# router.register(r'kudos-post', views.KudoPostViewSet)
router.register(r'kudos-received', views.KudoReceivedViewSet)
router.register(r'user-data', views.UserDataViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('kudos-post/', views.kudos_post),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('my-info/', MyInfo.as_view(), name='my_info'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
