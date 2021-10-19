from django.shortcuts import redirect, render

# Create your views here.
def pdf_explore(request):
    pass

def pdf_upload(request):
    if request.user.is_authenticated:
        uploaded_file = request.FILES['uploaded_pdf_file']
        
        return redirect('home')
    else:
        return redirect('login')

def pdf_upload_view(request):
    if request.user.is_authenticated:
        return render(request, 'pdf_pages/pdf_upload.html')
    else:
        return redirect('login')