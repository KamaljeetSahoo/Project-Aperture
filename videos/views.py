from django.shortcuts import redirect, render

import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from gallery.utils import generate_caption, generate_tags
from .models import Video, ExtractedFrame, FrameTag, FrameCaption
from .utils import extract_frames_from_video

# Create your views here.
def video_upload(request):
    if request.user.is_authenticated:
        return render(request, 'videos/upload_video.html')
    else:
        return redirect('login')

def handle_upload_video(request):
    if request.user.is_authenticated:
        vid = Video(video = request.FILES['uploaded_video_file'])
        vid.save()
        extract_frames_from_video(vid.video.path, num_frames=4)

        for file in os.listdir('temp_extracted_frames'):
            img = Image.open('temp_extracted_frames/'+file).convert('RGB')
            img_io = BytesIO()
            img.save(img_io, format="JPEG", quality=100)
            img_content = ContentFile(img_io.getvalue(), file)
            img = ExtractedFrame(image = img_content)
            img.save()
            vid.extracted_image.add(img)

            _, captions = generate_caption(img.image.url)
            for cap in captions:
                new_cap = FrameCaption(description = cap)
                new_cap.save()
                img.caption.add(new_cap)
            
            tags = generate_tags(img.image.url)
            for tag in tags:
                if not FrameTag.objects.filter(tag_name=tag).exists():
                    new_tag = FrameTag(tag_name = tag)
                    new_tag.save()
                    img.tag.add(new_tag)
                else:
                    t = FrameTag.objects.get(tag_name = tag)
                    img.tag.add(t)


        return redirect('browse_videos')
    else:
        return redirect('login')

def browse_videos(request):
    if request.user.is_authenticated:
        videos = Video.objects.all()
        context = {
            'videos': videos
        }
        return render(request, 'videos/browse_videos.html', context=context)
    else:
        return redirect('login')

def view_single_video_content(request, video_id):
    if request.user.is_authenticated:
        video = Video.objects.get(id=video_id)
        context = {
            'video': video,
        }
        return render(request, 'videos/single_view_video.html', context=context)
    else:
        return redirect('login')