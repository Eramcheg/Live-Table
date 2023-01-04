from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.generic import TemplateView
from .models import FileModel

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        print(request)
        return render(request, 'index.html')

    def post(self, request):
        print(request.POST['file'])
        return render(request, 'index.html')
        '''form = UploadFileForm(request.POST, request.FILES)
        print(request.POST['file'])
        return render(request, 'index.html', context={'fileform': UploadFileForm})'''

def index_page(request):
    return render(request, 'index.html')
