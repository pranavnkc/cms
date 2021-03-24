import json
from rest_framework import serializers

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    categories = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )

    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ("author", )
        extra_kwargs = {
            "document": {"required": True}
        }

    def create(self, validated_data, *args, **kwargs):
        validated_data["author"] = self.context["request"].user
        return super(ContentSerializer, self).create(validated_data, *args, **kwargs)

    def to_representation(self, obj):
        ret = super(ContentSerializer, self).to_representation(obj)
        ret["categories"] = json.loads(obj.categories.replace("'", '"'))
        return ret
