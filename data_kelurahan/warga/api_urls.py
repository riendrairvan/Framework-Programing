from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet
# from .views import WargaListAPIView, WargaDetailAPIView, PengaduanDetailAPIView

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')
urlpatterns = [
    # path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    # path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
    # path('pengaduan', PengaduanDetailAPIView.as_view(), name='pengaduan-detail'),
    path('', include(router.urls)),
]