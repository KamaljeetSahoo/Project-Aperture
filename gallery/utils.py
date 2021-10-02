from decouple import config
import requests
from django.conf import settings

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