from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = ""
endpoint = ""

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_url = "https://i.imgur.com/gJTXssF.jpg"

response = cv_client.describe_image(
    url= image_url,
    raw=True
)


print(response.response.json())