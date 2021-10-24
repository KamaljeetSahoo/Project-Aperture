from django.shortcuts import render

# Create your views here.
def video_upload(request):
    return render(request, 'videos/upload_video.html')

def browse_videos(request):
    return render(request, 'videos/browse_videos.html')

def view_single_video_content(request, video_id):
    pass