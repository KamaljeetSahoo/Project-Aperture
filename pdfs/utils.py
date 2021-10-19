import PyPDF2, random
from PIL import Image
from django.conf import settings
import os

from .models import PDF_File, PDF_Caption, PDF_Tag, ExtractedImage
from gallery.utils import generate_tags

alpha = []
for i in range(26):
    alpha += [chr(ord('a')+ i)]

def generate():
    string =  ''.join(random.sample(alpha,k=5))
    return string


def make_custom_file_name_jpg(file_name):
    while True:
        print(file_name)
        if os.path.exists(os.path.join(file_name)):
            aux = generate()
            file_name = file_name.split('.')[0]+ '_' + aux + '.jpg'
        else:
            return file_name

def make_custom_file_name_png(file_name):
    while True:
        print(file_name, "asuchi")
        if os.path.exists(os.path.join(file_name)):
            aux = generate()
            file_name = file_name.split('.')[0]+ '_' + aux + '.png'
        else:
            return file_name

def extract_images(file_path):
    absolute_path = str(settings.BASE_DIR) + file_path
    print(absolute_path)
    pdf_file = PyPDF2.PdfFileReader(open(absolute_path, "rb"))
    new_files = []
    for i in range(pdf_file.numPages):
        page = pdf_file.getPage(i)
        try:
            xObject = page['/Resources']['/XObject'].getObject()
            
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj]._data
                    if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"
                    if xObject[obj]['/Filter'] == '/FlateDecode':
                        try:
                            img = Image.frombytes(mode, size, data)
                            file_name = 'extracted_images/'+obj[1:] + ".png"
                            file_name = make_custom_file_name_png(file_name)
                            new_files.append(file_name)
                            print(file_name, "changed")
                            img.save(file_name)
                            img.close()
                        except:
                            pass
                    elif xObject[obj]['/Filter'] == '/DCTDecode':
                        try:
                            file_name = 'extracted_images/'+obj[1:] + ".jpg"
                            file_name = make_custom_file_name_jpg(file_name)
                            new_files.append(file_name)
                            print(file_name, "changed")
                            img = open(file_name, "wb")
                            img.write(data)
                            img.close()
                        except:
                            pass
        except:
            pass
    return new_files