from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import ImageFiles, AudioFiles
from .serializers import ImageFilesSerializer, AudioFilesSerializer

class ImageFilesUploadView(CreateAPIView):
    queryset = ImageFiles.objects.all()
    serializer_class = ImageFilesSerializer

class AudioFilesUploadView(CreateAPIView):
    queryset = AudioFiles.objects.all()
    serializer_class = AudioFilesSerializer
