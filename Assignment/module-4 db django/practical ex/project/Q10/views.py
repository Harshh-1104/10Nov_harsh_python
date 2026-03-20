from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # Simulate successful registration or handling
        return render(request, 'Q10/register.html', {'success': True})
    return render(request, 'Q10/register.html')
