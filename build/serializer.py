from rest_framework import serializers


class BuildSerializer(serializers.Serializer):

    where = serializers.CharField(max_length=1000, required=True, allow_blank=True,
                                  help_text="specify the where condition to query simpledb")
    limit = serializers.IntegerField(required=True, allow_null=True, max_value=100, min_value=1,
                                     help_text="specify the limit on output result")

    order_by = serializers.CharField(max_length=200, required=False, allow_null=True,
                                     allow_blank=True, help_text="Order by string.")

    next_token = serializers.CharField(required=False, allow_blank=True, default=None,
                                       help_text="Next token to load more data.")

    class Meta:
        fields = ('where', 'limit', 'order_by')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
