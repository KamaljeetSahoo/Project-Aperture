from django.shortcuts import render, redirect
from .models import Picture, Tag
from .forms import PictureForm

# Create your views here.
import random
alpha = []
for i in range(26):
    alpha += [chr(ord('a')+ i)]

def generate(n):
    res = []
    for i in range(n):
        n = random.randint(3,8)
        string =  ''.join(random.sample(alpha,k=n))
        res+= [string]
    return res


def contributeImageView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PictureForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                generated_tags = generate(4)
                new_tags = []
                for tag in generated_tags:
                    if not Tag.objects.filter(tag_name = tag).exists():
                        new_tag = Tag(tag_name = tag)
                        new_tag.save()
                        new_tags.append(new_tag)
                    else:
                        t = Tag.objects.get(tag_name = tag)
                        new_tags.append(t)
                obj = Picture(image=image)
                obj.save()
                for tag in new_tags:
                    obj.tag.add(tag)
        else:
            form = PictureForm()
        context = {
            'form' : form,
        }

        return render(request, 'pages/image_contribute.html', context=context)
    else:
        return redirect('login')

def homepage(request):
    if request.user.is_authenticated:
        pics = Picture.objects.all()
        final_list = []
        for img in pics:
            final_list.append([img, list(img.tag.all())])
        context = {
            'img': final_list
        }
        return render(request, 'pages/landing_page.html', context=context)
    return redirect('login')

def single_image_view(request, image_id):
    image = Picture.objects.get(id=image_id)
    context = {
        'img': image,
        'tags': image.tag.all()
    }
    return render(request, 'pages/single_view.html', context=context)