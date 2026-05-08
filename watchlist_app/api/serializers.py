from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    watchlist = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    avg_rating = serializers.StringRelatedField(read_only=True)
    number_rating = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
