from django.shortcuts import redirect, render
import os

from .models import PDF_File, PDF_Caption, PDF_Tag, ExtractedImage

from .utils import extract_images, similar_captions
from gallery.utils import generate_caption, generate_tags, correct_spell_and_meaning

# Create your views here.
def pdf_explore(request):
    pdfs = list(PDF_File.objects.all())
    context = {
        'pdfs': pdfs
    }
    return render(request, 'pdf_pages/pdf_explore.html', context=context)

def single_pdf_view(request, pdf_id):
    pdf = PDF_File.objects.get(id=pdf_id)
    context = {
        'pdf': pdf
    }
    return render(request, 'pdf_pages/single_view_pdf.html', context=context)

def pdf_upload(request):
    if request.user.is_authenticated:
        uploaded_file = request.FILES['uploaded_pdf_file']
        new_pdf = PDF_File(pdf=uploaded_file)
        new_pdf.save()
        new_imgs = extract_images(new_pdf.pdf.url)

        for file in new_imgs:
            new_img = ExtractedImage(image = os.path.join(file))
            new_img.save()

            _, captions = generate_caption(new_img.image.url)
            for cap in captions:
                new_cap = PDF_Caption(description = cap)
                new_cap.save()
                new_img.caption.add(new_cap)

            tags = generate_tags(new_img.image.url)
            for tag in tags:
                if not PDF_Tag.objects.filter(tag_name=tag).exists():
                    new_tag = PDF_Tag(tag_name = tag)
                    new_tag.save()
                    new_img.tag.add(new_tag)
                else:
                    t = PDF_Tag.objects.get(tag_name = tag)
                    new_img.tag.add(t)
                
            new_pdf.image.add(new_img)
        
        return redirect('home')
    else:
        return redirect('login')

def pdf_upload_view(request):
    if request.user.is_authenticated:
        return render(request, 'pdf_pages/pdf_upload.html')
    else:
        return redirect('login')

def edit_page_view(request, image_id):
    if request.user.is_authenticated:
        img = ExtractedImage.objects.get(id=image_id)
        context = {
            'img': img,
        }
        return render(request, 'pdf_pages/edit_caption_tags.html', context=context)
    else:
        return redirect('login')

def delete_tag_from_image(request, tag_id, image_id):
    if request.user.is_authenticated:
        img = ExtractedImage.objects.get(id=image_id)
        tag = PDF_Tag.objects.get(id=tag_id)
        img.tag.remove(tag)
        return redirect('edit_pdf_image_view', image_id=image_id)
    else:
        return redirect('login')

def add_tag_to_image(request, image_id):
    if request.user.is_authenticated:
        print(request.POST['new_tag'])
        img = ExtractedImage.objects.get(id=image_id)
        new_tag = request.POST['new_tag']
        if PDF_Tag.objects.filter(tag_name=new_tag).exists():
            img.tag.add(PDF_Tag.objects.get(tag_name = new_tag))
        else:
            new = PDF_Tag(tag_name = new_tag)
            new.save()
            img.tag.add(new)
        return redirect('edit_pdf_image_view', image_id=image_id)
    else:
        return render('login')

def update_caption_pdf_image(request, image_id):
    if request.user.is_authenticated:
        img = ExtractedImage(id=image_id)
        updated_caption = request.POST['updated_caption']
        if len(updated_caption) != 0:
            current_caption = list(img.caption.all())[0]
            current_caption.description = updated_caption
            current_caption.save()
            return redirect('edit_pdf_image_view', image_id=image_id)
        else:
            return redirect('edit_pdf_image_view', image_id=image_id)
    else:
        return redirect('login')

def search_pdf_view(request):
    if request.user.is_authenticated:
        return render(request, 'pdf_pages/pdf_search.html')
    else:
        return redirect('login')

def search_results_pdf(request):
    if request.user.is_authenticated:
        
        corrected = False

        search_query = request.POST['search'].lower()
        corrected_query = correct_spell_and_meaning(search_query)
        if corrected_query != search_query:
            corrected = True
        
        related_images = []
        if len(corrected_query.split(' ')) >= 1:
            #caption search
            related_captions = similar_captions(corrected_query)[0:5]
            for caption in related_captions:
                cap = PDF_Caption.objects.filter(description = caption)[0]
                for img in cap.extractedimage_set.all():
                    related_images.append(img)
        else:
            #tag search
            pass


        context = {
            'corrected': corrected,
            'search_results': True,
            'DidYouMean': corrected_query,
            'related_images': related_images
        }
        return render(request, 'pdf_pages/pdf_search.html', context=context)
    else:
        return redirect('login')