from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StreamPlatformVS, ReviewList, ReviewDetail, WatchListVS, ReviewCreate

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
router.register('list', WatchListVS, basename='list')

urlpatterns = [
    path('', include(router.urls)),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path(
        'stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'
    ),
    path(
        '<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'
    ),
]
