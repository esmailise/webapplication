from django.shortcuts import render , redirect , HttpResponseRedirect
from django.urls import reverse 
from .models import Blog ,Tag ,Category , Comment
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def blog_list(request):
    
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number  = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    
    contex={
        "blog_obj":blog_obj
    }

    return render(request, "blog/blog_list.html",contex)

def blog_detail(request,id):

    
    blog = Blog.objects.get(id = id)
    tags = Tag.objects.all().filter(blogs = blog)
    recents = Blog.objects.all().order_by("-created_at")[:5]
    categories = Category.objects.all()
    comments = Comment.objects.all().filter(blog = blog)

    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']

            new_comment = Comment(blog=blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()
            messages.success(request, 'با موفقیت ثبت شد ')
            return HttpResponseRedirect(reverse('blog:detail', kwargs = {'id':id}))
            
                        
    else:
        form = CommentForm()
        

    contex ={
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments,
         
    }

    return render(request,"blog/blog_detail.html",contex)



def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug = tag)

    paginator = Paginator(blogs, 3)
    page_number  = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    
    contex={
        "blog_obj":blog_obj
    }

    return render(request, "blog/blog_list.html",contex)



def blog_category(request,categorys):
    
    blogs = Blog.objects.filter(category__slug = categorys)

    paginator = Paginator(blogs, 3)
    page_number  = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)

    contex = {
        "blog_obj":blog_obj
    }

    return render(request, "blog/blog_list.html",contex)

def search (request):
    
    if request.method == 'GET':
        q = request.GET.get("search")

    blog_search = Blog.objects.filter(title__icontains = q)

    paginator = Paginator(blog_search, 3)
    page_number  = request.GET.get('page')
    blog_obj = paginator.get_page(page_number) 

    return render(request,"blog/blog_list.html",{"blog_obj":blog_obj})
    
    