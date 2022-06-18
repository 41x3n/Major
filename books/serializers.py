from rest_framework import serializers
from .models import Books, Collections


class BookSerializer(serializers.ModelSerializer):
    added_by_user = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Books
        fields = ("pk", "key", "title", "year", "cover_i", "added_by_user")
