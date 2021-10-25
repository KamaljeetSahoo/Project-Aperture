from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
from django.conf import settings

diskwriter = KeyFrameDiskWriter(location="temp_extracted_frames")

def extract_frames_from_video(video_path, num_frames):
    vd = Video()
    vd.extract_video_keyframes(
       no_of_frames=num_frames, file_path=video_path,
       writer=diskwriter) 