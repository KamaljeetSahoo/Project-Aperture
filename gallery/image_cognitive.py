from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from decouple import config

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = config('SUBSCRIPTION_KEY')
endpoint = config('ENDPOINT')

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_url = "https://i.imgur.com/gJTXssF.jpg"

response = cv_client.describe_image(
    url= image_url,
    raw=True
)


print(response.response.json())