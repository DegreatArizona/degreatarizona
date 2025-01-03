from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})
    
def blog(request):
    return render(request, 'blog.html', {})
    
def contact(request):
    return render(request, 'contact.html', {})
    
def product(request):
    return render(request, 'product.html', {})
    
def project(request):
    return render(request, 'project.html', {})
    
def quote(request):
    return render(request, 'quote.html', {})
    
def service(request):
    return render(request, 'service.html', {})
    
def training(request):
    return render(request, 'training.html', {})
    