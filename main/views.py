from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def event(request):
    return render(request, 'event.html')

def blog(request):
    return render(request, 'blog.html')

def book(request):
    return render(request, 'book.html')

def menu(request):
    return render(request, 'menu.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def error_404(request):
    return render(request, '404.html')
