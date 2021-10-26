from django.shortcuts import redirect, render

import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from gallery.utils import generate_caption, generate_tags, correct_spell_and_meaning
from .models import Video, ExtractedFrame, FrameTag, FrameCaption
from .utils import extract_frames_from_video, similar_frame_captions

# Create your views here.


def video_upload(request):
    if request.user.is_authenticated:
        return render(request, 'videos/upload_video.html')
    else:
        return redirect('login')


def handle_upload_video(request):
    if request.user.is_authenticated:
        vid = Video(video=request.FILES['uploaded_video_file'])
        vid.save()
        extract_frames_from_video(vid.video.path, num_frames=4)

        for file in os.listdir('temp_extracted_frames'):
            img = Image.open('temp_extracted_frames/'+file).convert('RGB')
            img_io = BytesIO()
            img.save(img_io, format="JPEG", quality=100)
            img_content = ContentFile(img_io.getvalue(), file)
            img = ExtractedFrame(image=img_content)
            img.save()
            vid.extracted_image.add(img)

            _, captions = generate_caption(img.image.url)
            for cap in captions:
                new_cap = FrameCaption(description=cap)
                new_cap.save()
                img.caption.add(new_cap)

            tags = generate_tags(img.image.url)
            for tag in tags:
                if not FrameTag.objects.filter(tag_name=tag).exists():
                    new_tag = FrameTag(tag_name=tag)
                    new_tag.save()
                    img.tag.add(new_tag)
                else:
                    t = FrameTag.objects.get(tag_name=tag)
                    img.tag.add(t)
        to_be_removed = os.listdir('temp_extracted_frames')
        for file in to_be_removed:
            os.remove('temp_extracted_frames/'+file)

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


def edit_video_frame_view(request, image_id):
    if request.user.is_authenticated:
        context = {
            'img': ExtractedFrame.objects.get(id=image_id)
        }
        return render(request, 'videos/edit_contents.html', context=context)
    else:
        return redirect('login')


def add_tag_video_frame(request, image_id):
    if request.user.is_authenticated:
        img = ExtractedFrame.objects.get(id=image_id)
        new_tag = request.POST['new_tag']
        if FrameTag.objects.filter(tag_name=new_tag).exists():
            img.tag.add(FrameTag.objects.get(tag_name=new_tag))
        else:
            new = FrameTag(tag_name=new_tag)
            new.save()
            img.tag.add(new)
        return redirect('edit_video_frame', image_id=image_id)
    else:
        return render('login')


def delete_tag_video_frame(request, tag_id, image_id):
    if request.user.is_authenticated:
        img = ExtractedFrame.objects.get(id=image_id)
        tag = FrameTag.objects.get(id=tag_id)
        img.tag.remove(tag)
        return redirect('edit_video_frame', image_id=image_id)
    else:
        return redirect('login')


def update_caption_video_frame(request, image_id):
    if request.user.is_authenticated:
        img = ExtractedFrame(id=image_id)
        updated_caption = request.POST['updated_caption']
        if len(updated_caption) != 0:
            current_caption = list(img.caption.all())[0]
            current_caption.description = updated_caption
            current_caption.save()
            return redirect('edit_video_frame', image_id=image_id)
        else:
            return redirect('edit_video_frame', image_id=image_id)
    else:
        return redirect('login')


def video_search_view(request):
    if request.user.is_authenticated:
        return render(request, 'videos/video_search.html')
    else:
        return redirect('login')


def video_search_results(request):
    if request.user.is_authenticated:
        corrected = False

        search_query = request.POST['search'].lower()
        corrected_query = correct_spell_and_meaning(search_query)
        if corrected_query != search_query:
            corrected = True

        related_images = []
        if len(corrected_query.split(' ')) >= 1:
            # caption search
            related_captions = similar_frame_captions(corrected_query)[0:5]
            for caption in related_captions:
                cap = FrameCaption.objects.filter(description=caption)[0]
                for img in cap.extractedframe_set.all():
                    related_images.append(img)
        else:
            # tag search
            pass

        context = {
            'corrected': corrected,
            'search_results': True,
            'DidYouMean': corrected_query,
            'related_images': related_images
        }
        return render(request, 'videos/video_search.html', context=context)
    else:
        return redirect('login')
