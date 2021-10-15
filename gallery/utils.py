from decouple import config
import requests
from django.conf import settings
from gingerit.gingerit import GingerIt
from .models import Tag

#similar tag libs
from gensim.test.utils import common_texts
import gensim.downloader
from gensim.models import Word2Vec

glove_vectors = gensim.downloader.load('glove-twitter-50')
model = Word2Vec(sentences=common_texts , window=5, min_count=1, workers=4)


ginger_parser = GingerIt()

subscription_key = config('SUBSCRIPTION_KEY')
endpoint = config('ENDPOINT')
endpoint_describe = config('ENDPOINT_DESCRIBE')

def generate_tags(url):
    image_data = open(str(settings.BASE_DIR)+url, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/octet-stream'}
    response = requests.post(endpoint, headers=headers, data=image_data)
    response = response.json()
    tags = []
    for i in response['tags']:
        tags.append(i['name'])
    return tags

def generate_caption(url):
    image_data = open(str(settings.BASE_DIR)+url, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/octet-stream'}
    response = requests.post(endpoint_describe, headers=headers, data=image_data)
    response = response.json()
    tags = []
    captions = []
    for i in response['description']['tags']:
        tags.append(i)
    for i in response['description']['captions']:
        captions.append(i['text'])
    return tags, captions

def reverse_image_generate_tags(image):
    image_data = image.read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
    response = requests.post(endpoint, headers=headers, data=image_data)
    response = response.json()
    tags = []
    for i in response['tags']:
        tags.append(i['name'])
    return tags

def correct_spell_and_meaning(sentence):
    return ginger_parser.parse(sentence)['result'].lower()


def find_similar_tags(ref_word):
    tags = list(Tag.objects.all().values_list('tag_name', flat=True))
    res = []
    if len(ref_word.split(" ")) == 1:
        for word in tags:
            try:
                res.append([word,glove_vectors.similarity(ref_word,word)])
            except:
                pass
    else:
        for word in tags:
            try:
                res.append([word,glove_vectors.similarity(ref_word.split(" ")[-1],word)])
            except:
                pass
    res = sorted( res, key = lambda res : res[1],reverse = True )
    top_tags = []
    top = 8
    for i in range(len(res)):
        top-=1
        if not top:
            break
        top_tags.append(res[i][0])
    final_tags = []
    for i in range(len(top_tags)):
        final_tags.append(Tag.objects.get(tag_name=top_tags[i]))
    return final_tags
    


# =================== Aurtomation ===================
import os
from .models import Picture, Tag
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def automate_upload(folder_path):
    files = os.listdir(folder_path)
    print("Process Started =============")
    for file in files:
        print(file)
        if file[-3:] == 'jpg':
            img_io = BytesIO()
            path = os.path.join(folder_path, file)
            curr_image = Image.open(path).convert('RGB')
            curr_image.save(img_io, format="JPEG", quality=100)
            img_content = ContentFile(img_io.getvalue(), file)
            image_obj = Picture(image = img_content)
            image_obj.save()
            generated_tags = generate_tags(image_obj.image.url)
            new_tags = []
            for tag in generated_tags:
                if not Tag.objects.filter(tag_name = tag).exists():
                    new_tag = Tag(tag_name = tag)
                    new_tag.save()
                    new_tags.append(new_tag)
                else:
                    t = Tag.objects.get(tag_name = tag)
                    new_tags.append(t)
            for tag in new_tags:
                image_obj.tag.add(tag)
            os.remove(path)


def auxilary_delete_files():
    s = ['black and silver claw hammer.jpg',
        'brown deer under tree.jpg',
        'beige candle lot.jpg',
        'assorted-type of vegetables.jpg',
        'black traffic light.jpg',
        'architectural photography of modern building.jpg',
        'assorted candies.jpg',
        'black and white cruise ship sailing on sea.jpg',
        'black traffic light turned on during night time.jpg',
        'art30.jpg',
        'assorted pen and colored papers in organizer case.jpg',
        'body of water during daytime.jpg',
        'black digital device at 0 00.jpg',
        'assorted planet decor.jpg',
        'bunch of raspberry and grapes.jpg',
        'brown and black floral curtains near green leafed trees.jpg',
        'assorted-color paintbrushes.jpg',
        'assorted petaled flowers centerpiece inside room.jpg',
        'blue and white abstract painting.jpg',
        'brown fox on snow field.jpg',
        'brown makeup brush in front pink powder on glass case.jpg',]
    
    for i in s:
        os.remove(os.path.join('/Users/kamaljeet/Desktop/test_images', i))