from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

# View to list all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Q11/doctor_list.html', {'doctors': doctors})

# View to add or edit a doctor record
def add_edit_doctor(request, pk=None):
    if pk:
        doctor = get_object_or_404(Doctor, pk=pk)
    else:
        doctor = None
        
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_crud_list')
    else:
        form = DoctorForm(instance=doctor)
    
    return render(request, 'Q11/doctor_form.html', {'form': form, 'doctor': doctor})

# View to delete a doctor record
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_crud_list')
    return render(request, 'Q11/confirm_delete.html', {'doctor': doctor})
