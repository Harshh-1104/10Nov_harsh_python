from django.shortcuts import render

def home(request):
    """Home page view."""
    return render(request, 'Q9/home.html', {
        'title': 'Q9 - Home',
        'message': 'Welcome to the Q9 Django project',
    })

def about(request):
    """About page view."""
    return render(request, 'Q9/about.html', {
        'title': 'Q9 - About',
        'content': 'This is the about page.',
    })

def contact(request):
    """Contact page view."""
    return render(request, 'Q9/contact.html', {
        'title': 'Q9 - Contact',
        'email': 'chv@gmail.com',
        'phone': '9876543210',
    })

def services(request):
    """Services page view."""
    services_list = [
        'Web Development',
        'Mobile Apps',
        'Data Analysis',
        'Consulting',
    ]
    return render(request, 'Q9/services.html', {
        'title': 'Q9 - Services',
        'services': services_list,
    })

