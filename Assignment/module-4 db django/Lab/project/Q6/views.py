from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Q6/doctor_list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('q6_home')
    else:
        form = DoctorForm()
    return render(request, 'Q6/doctor_form.html', {'form': form})

