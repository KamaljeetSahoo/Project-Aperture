from django.shortcuts import render

# Create your views here.
def contributeImageView(request):
    return render(request, 'pages/image_contribute.html')