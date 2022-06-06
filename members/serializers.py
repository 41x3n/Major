from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Member
        fields = ("pk", "first_name", "last_name", "email", "added_by")
