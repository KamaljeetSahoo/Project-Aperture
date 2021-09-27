from django.shortcuts import render
from .models import Picture
from .forms import PictureForm

# Create your views here.
def contributeImageView(request):
    form = PictureForm()
    context = {
        'form' : form
    }
    return render(request, 'pages/image_contribute.html', context=context)