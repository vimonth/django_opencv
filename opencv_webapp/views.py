from django.shortcuts import render
from .forms import SimpleUploadForm
from .cv_functions import cv_detect_face

# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html',{})

def simple_upload(request):
    if request.method == 'POST':
        # print(request.POST)
        form = SimpleUploadForm(request.POST, request.FILES)

    if form.is_valid():
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        context = {'form':form, 'uploaded_file_url':uploaded_file_url}
        return render(request, 'opencv_webapp/simple_upload.html', context)

    else: #get 요청일때
        form = SimpleUploadForm()
        context = {'form' : form}
        return render(request, 'opencv_webapp/simple_upload.html', context)
