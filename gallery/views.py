from django.shortcuts import render, redirect
from .models import Picture
from .forms import PictureForm

# Create your views here.
def contributeImageView(request):
    if request.user.is_authenticated:
        form = PictureForm()
        context = {
            'form' : form
        }
        if request.method == "POST":
            form = PictureForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                obj = Picture(image=image)
                obj.save()
        
        else:
            form = PictureForm()
        
        context = {
            'form' : form,
        }

        return render(request, 'pages/image_contribute.html', context=context)
    else:
        return redirect('login')

def landig_view(request):
    pics = Picture.objects.all()
    context = {
        'pics': pics
    }
    return render(request, 'pages/landing_page.html', context=context)

def single_image_view(request, image_id):
    image = Picture.objects.get(id=image_id)
    context = {
        'img': image
    }
    return render(request, 'pages/single_view.html', context=context)