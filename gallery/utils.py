from decouple import config
import requests
from django.conf import settings
from gingerit.gingerit import GingerIt

ginger_parser = GingerIt()

subscription_key = config('SUBSCRIPTION_KEY')
endpoint = config('ENDPOINT')

def generate_tags(url):
    image_data = open(str(settings.BASE_DIR)+url, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
    response = requests.post(endpoint, headers=headers, data=image_data)
    response = response.json()
    tags = []
    for i in response['tags']:
        tags.append(i['name'])
    return tags

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