from django.shortcuts import render,HttpResponseRedirect
from .form import imageforms
from .models import imagemodel
# Create your views here.
def imageviews(request):
    if request.method == "POST":
        fm = imageforms(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = imageforms()
    img = imagemodel.objects.all()    
    return render(request, 'myapp/imageupload.html',{'img':img,'form':fm})
