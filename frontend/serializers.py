from rest_framework import serializers

from frontend.models import Settings


class SettingsSerializer(serializers.ModelSerializer):
    port = serializers.SerializerMethodField()
    batch_size = serializers.SerializerMethodField()
    ip_address = serializers.SerializerMethodField()
    fps = serializers.SerializerMethodField()

    class Meta:
        model = Settings
        fields = ('port', 'batch_size', 'ip_address', 'fps')

    def get_port(self, obj):
        return obj.port

    def get_batch_size(self, obj):
        return obj.batch_size

    def get_ip_address(self,obj):
        return obj.ip_address

    def get_fps(self,obj):
        return obj.fps