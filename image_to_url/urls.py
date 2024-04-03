from django.urls import path
from .views import AudioFilesUploadView, ImageFilesUploadView

urlpatterns = [
    path('', ImageFilesUploadView.as_view(), name='upload_image'),
    path('upload/audio/', AudioFilesUploadView.as_view(), name='upload_audio'),
    
]
