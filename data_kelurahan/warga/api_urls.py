from django.urls import path
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanDetailAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
    path('pengaduan', PengaduanDetailAPIView.as_view(), name='pengaduan-detail'),
]
