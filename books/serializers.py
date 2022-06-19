from rest_framework import serializers
from .models import Books, Collections


class BookSerializer(serializers.ModelSerializer):
    added_by_user = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Books
        fields = ("key", "title", "year", "cover_i", "added_by_user")


class CollectionSerializer(serializers.ModelSerializer):
    book_key = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())
    user_id = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Collections
        fields = ("book_key", "user_id")
