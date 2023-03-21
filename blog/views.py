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