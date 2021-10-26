from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter

from .models import FrameCaption
from gallery.utils import sentence_similarity_model
from sklearn.metrics.pairwise import cosine_similarity

diskwriter = KeyFrameDiskWriter(location="temp_extracted_frames")


def extract_frames_from_video(video_path, num_frames):
    vd = Video()
    vd.extract_video_keyframes(
        no_of_frames=num_frames, file_path=video_path,
        writer=diskwriter)


def similar_frame_captions(searched_caption):
    all_captions = list(FrameCaption.objects.all(
    ).values_list('description', flat=True))
    all_captions_vecs = sentence_similarity_model.encode(all_captions)
    searched_vec = sentence_similarity_model.encode([searched_caption])
    similarities = cosine_similarity(searched_vec, all_captions_vecs)
    vectors_with_similarity_factor = [
        [similarities[0][i], all_captions[i]] for i in range(len(similarities[0]))]
    vectors_with_similarity_factor = sorted(
        vectors_with_similarity_factor, key=lambda x: x[0], reverse=True)
    sorted_captions = [i[1] for i in vectors_with_similarity_factor]
    return sorted_captions
