from django.shortcuts import redirect, render
import os

from .models import PDF_File, PDF_Caption, PDF_Tag, ExtractedImage

from .utils import extract_images
from gallery.utils import generate_caption, generate_tags

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
    img = ExtractedImage.objects.get(id=image_id)
    context = {
        'img': img,
    }
    return render(request, 'pdf_pages/edit_caption_tags.html', context=context)

def delete_tag_from_image(request, tag_id, image_id):
    pass

def add_tag_to_image(request, image_id):
    pass