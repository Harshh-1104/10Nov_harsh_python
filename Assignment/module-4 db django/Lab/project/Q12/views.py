from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def product_list(request):
    """Read: List all products using Django ORM."""
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'Q12/product_list.html', {
        'products': products,
        'title': 'Q12 - CRUD Operations with Django ORM',
    })

def product_create(request):
    """Create: Add a new product using Django ORM."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # ORM create operation
            messages.success(request, 'Product created successfully!')
            return redirect('q12_home')
    else:
        form = ProductForm()
    return render(request, 'Q12/product_form.html', {
        'form': form,
        'action': 'Create',
    })

def product_update(request, pk):
    """Update: Modify an existing product using Django ORM."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()  # ORM update operation
            messages.success(request, 'Product updated successfully!')
            return redirect('q12_home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'Q12/product_form.html', {
        'form': form,
        'action': 'Update',
        'product': product,
    })

def product_delete(request, pk):
    """Delete: Remove a product using Django ORM."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()  # ORM delete operation
        messages.success(request, 'Product deleted successfully!')
        return redirect('q12_home')
    return render(request, 'Q12/product_confirm_delete.html', {
        'product': product,
    })

