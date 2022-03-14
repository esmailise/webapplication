from django.shortcuts import render
from .models import AboutUs
from works.models import works,Category
# Create your views here.
def aboutus(request):
    about = AboutUs.objects.all()
    works_list = works.objects.all()
    category = Category.objects.all()
    contex={
        "about":about,
        'works' : works_list, 
        'category' : category,
    }

    return render(request, 'aboutus/about.html',contex)