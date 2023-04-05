from aosoiy.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

schema_view = get_schema_view(
   openapi.Info(
      title="Suv Servis API Do",
      default_version='v1',
      description="Imtihondagi SuvAPI",
      contact=openapi.Contact(email="Qodirbek Shokirbekov, <qodirbekshokirbekov@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register("suvlar", SuvViewSet)
router.register("mijozlar", MijozViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('adminlar/', AdminAPI.as_view()),
    path('adminlar/<int:pk>/', AdminDetailAPI.as_view()),
    path('buyurtmalar/', BuyurtmaAPI.as_view()),
    path('buyurtma/<int:pk>/', BuyurtmaDetailAPI.as_view()),
    path('haydovchilar/', HaydovchiAPI.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiDetailAPI.as_view()),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
