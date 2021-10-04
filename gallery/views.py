from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Picture, Tag
from .forms import PictureForm
from .utils import generate_tags, reverse_image_generate_tags

# Create your views here.
# import random
# alpha = []
# for i in range(26):
#     alpha += [chr(ord('a')+ i)]

# def generate(n):
#     res = []
#     for i in range(n):
#         n = random.randint(3,8)
#         string =  ''.join(random.sample(alpha,k=n))
#         res+= [string]
#     return res


def contributeImageView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PictureForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                obj = Picture(image=image)
                obj.save()

                generated_tags = generate_tags(obj.image.url)
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
                    obj.tag.add(tag)

                return redirect("edit_image", image_id=obj.id)
        else:
            form = PictureForm()
        context = {
            'form' : form,
        }

        return render(request, 'pages/image_contribute.html', context=context)
    else:
        return redirect('login')

def after_upload_view(request, image_id):
    if request.user.is_authenticated:
        context = {
            'img': Picture.objects.get(id=image_id)
        }
        return render(request, 'pages/edit_tags_intermediate.html', context=context)
    return redirect("login")

def homepage(request):
    if request.user.is_authenticated:
        pics = Picture.objects.all()
        context = {
            'img': pics
        }
        return render(request, 'pages/landing_page.html', context=context)
    return redirect('login')

def single_image_view(request, image_id):
    if request.user.is_authenticated:
        image = Picture.objects.get(id=image_id)
        context = {
            'img': image,
            'tags': image.tag.all()
        }
        return render(request, 'pages/single_view.html', context=context)
    return redirect("login")

def delete_tag_from_image(request, tag_id, image_id):
    if request.user.is_authenticated:
        img = Picture.objects.get(id=image_id)
        tag = Tag.objects.get(id=tag_id)
        img.tag.remove(tag)
        return redirect("edit_image", image_id=image_id)
    return redirect("login")

def add_tag_to_image(request, image_id):
    if request.user.is_authenticated:
        img = Picture.objects.get(id = image_id)
        new_tag_name = request.POST['new_tag']
        if not Tag.objects.filter(tag_name = new_tag_name).exists():
            tag = Tag(tag_name = new_tag_name)
            tag.save()
            img.tag.add(tag)
            return redirect("edit_image", image_id=image_id)
        else:
            tag = Tag.objects.get(tag_name = new_tag_name)
            img.tag.add(tag)
            return redirect("edit_image", image_id=image_id)
    else:
        return redirect("login")

def tag_based_image_search(request):
    search = request.GET['search_tag']
    search_keywords = search.split(" ")
    img = []
    for word in search_keywords:
        tag = Tag.objects.filter(tag_name__startswith = word)
        for t in tag:
            img += list(t.picture_set.all())
    if len(img) == 0:
        return redirect('home')
    context = {
            'img': set(img)
        }
    return render(request, 'pages/search_results.html', context=context)

def tag_click_search(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    context = {
        'img': tag.picture_set.all()
    }
    return render(request, 'pages/tag_click_search.html', context=context)

def reverse_image_search(request):
    if request.user.is_authenticated:
        image = request.FILES['search_image']
        generated_tags = reverse_image_generate_tags(image)
        img = []
        for tag in generated_tags:
            out = Tag.objects.filter(tag_name__startswith = tag)
            for t in out:
                img += list(t.picture_set.all())
        if len(img) == 0:
            return HttpResponse("Image kichi nahin")
        else:
            context = {
                'img': set(img)
            }
            return render(request, 'pages/search_results.html', context=context)
    else:
        return redirect('login')