from django.shortcuts import render
from .models import works , Gallery,Category
from aboutus.models import AboutUs
# Create your views here.

def works_list (request):
    categorys = Category.objects.all()
    works_list = works.objects.all()
    gallery = Gallery.objects.all()
    about = AboutUs.objects.all()

       
    contex = {
        'works' : works_list, 
        'gallery' : gallery,
        'category' : categorys,
        'about' : about,
    }
    return render(request,'works/index.html',contex)

