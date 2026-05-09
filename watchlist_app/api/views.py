from watchlist_app.models import Review, WatchList, StreamPlatform
from .serializers import ReviewSerializer, WatchListSerializer, StreamPlatformSerializer
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnlyOrAdmin
from rest_framework.response import Response


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        # checking exist review repeated
        review_queryset = Review.objects.filter(
            watchlist=watchlist, review_user=review_user

        )
        if review_queryset.exists():
            raise ValueError('You have already reviewed this movie!')

        # generate avarage some rating reviews
        if watchlist.number_rating == 0:
            # first add rating in value's average
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = watchlist.avg_rating + \
                serializer.validated_data['rating']/2
        # add data of number rating
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        # save review
        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnlyOrAdmin]


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


class WatchListVS(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAdminOrReadOnly]
