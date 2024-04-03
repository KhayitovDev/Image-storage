from rest_framework import serializers
from .models import ImageFiles, AudioFiles

class ImageFilesSerializer(serializers.ModelSerializer):
    file=serializers.FileField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = ImageFiles
        fields = ('id', 'file')

class AudioFilesSerializer(serializers.ModelSerializer):
    file=serializers.FileField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = AudioFiles
        fields = ('id', 'file')
