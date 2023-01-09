from django.urls import path
from kitablar.api import views as api_views
urlpatterns = [
    path('kitablar/', api_views.KitabListCreateAPIView.as_view(),name="kitab-listesi"),
    path('kitablar/<int:pk>', api_views.KitabDetailAPIView.as_view(),name="kitab-bilgileri"),
    path('kitablar/<int:kitab_pk>/yorum_yaz', api_views.YorumCreateAPIView.as_view(),name="yorum-yaz"),
    path('yorumlar/<int:pk>', api_views.YorumDetaulAPIView.as_view(),name="yorumlar"),
]
