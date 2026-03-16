from django.shortcuts import render


def home(request):
    """Render a simple webpage using Django's template renderer."""
    return render(request, 'Q4/home.html', {
        'title': 'Q4 - Simple Django Page',
        'message': 'This page is rendered using Django’s built-in template tooling.',
    })
