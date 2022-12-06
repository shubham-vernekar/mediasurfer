from rest_framework import serializers
from .models import Video

class VideoListSerializer(serializers.ModelSerializer):

    series = serializers.SerializerMethodField(read_only=True)
    badge = serializers.SerializerMethodField(read_only=True)
    special_tag = serializers.SerializerMethodField(read_only=True)
    subtitle_badge = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'title', 
            'categories', 
            'cast', 
            'views', 
            'favourite', 
            'duration', 
            'created', 
            'size', 
            'preview',
            'preview_thumbnail',
            'subtitle_badge',
            'width', 
            'height', 
            'tags', 
            'series', 
            'progress', 
            'last_viewed',
            'badge',
            'special_tag',
        ]

    def get_series(self, obj):
        if obj.series:
            return {
                "id": obj.series.id,
                "name": obj.series.name,
            }
        else:
            return None

    def get_special_tag(self, obj):
        return obj.get_special_tag()

    def get_badge(self, obj):
        return obj.get_badge()

    def get_subtitle_badge(self, obj):
        return obj.get_subtitle_badge()


class VideoSerializer(serializers.ModelSerializer):

    video_url = serializers.SerializerMethodField(read_only=True)
    subtitle_url = serializers.SerializerMethodField(read_only=True)
    series = serializers.SerializerMethodField(read_only=True)
    badge = serializers.SerializerMethodField(read_only=True)
    special_tag = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'title', 
            'video_url',
            'categories', 
            'cast', 
            'views', 
            'favourite', 
            'description', 
            'duration', 
            'created', 
            'size',  
            'poster',
            'subtitle_url',
            'scrubber_sprite', 
            'scrubber_vtt', 
            'width', 
            'height', 
            'tags', 
            'series', 
            'progress', 
            'last_viewed',
            'badge',
            'special_tag',
        ]

    def get_video_url(self, obj):
        return obj.get_video_url()

    def get_badge(self, obj):
        return obj.get_badge()

    def get_special_tag(self, obj):
        return obj.get_special_tag()

    def get_subtitle_url(self, obj):
        return obj.get_subtitle_url()

    def get_series(self, obj):
        if obj.series:
            return {
                "id": obj.series.id,
                "name": obj.series.name,
            }
        else:
            return None
