from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPostForm
from .models import BlogPostModel

# Create your views here.


def add_blog(request):
    
    if request.method == 'POST' : # and request.FILES['image']
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save() 
        return redirect('/') # see_blog
    else:
        form = BlogPostForm()
 
    context = {'form': form}
    template_name = ''
    return render(request, template_name, context)


def blog_detail(request, slug):
    template_name = ''
    context = {}
    try:
        blog_obj = get_object_or_404(BlogPostModel, slug=slug)
        context['blog_obj'] = blog_obj
    except Exception as e:
        raise e
    return render(request, template_name, context)


def blog_update(request, slug):
    context = {}
    template_name = ''

    blog_obj = BlogPostModel.objects.get(slug=slug)

    initial_dict = blog_obj
    form = BlogPostForm(instance=blog_obj)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_obj)
   
        if form.is_valid():
            blog_obj = form.save()
            blog_obj.save()

            return redirect('/')
        
    context['blog_obj'] = blog_obj
    context['form'] = form
    return render(request, template_name, context)


def blog_delete(request, slug):
    blog_obj = BlogPostModel.objects.get(slug=slug)
    print(blog_obj)

    if request.user.is_authenticated:
        blog_obj.delete()

    return redirect('/')



def add_blog(request):
    
    if request.method == 'POST' : # and request.FILES['image']
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save() 
        return redirect('/') # see_blog
    else:
        form = BlogPostForm()
 
    context = {'form': form}
    template_name = ''
    return render(request, template_name, context)


def blog_detail(request, slug):
    template_name = ''
    context = {}
    try:
        blog_obj = get_object_or_404(BlogPostModel, slug=slug)
        context['blog_obj'] = blog_obj
    except Exception as e:
        raise e
    return render(request, template_name, context)