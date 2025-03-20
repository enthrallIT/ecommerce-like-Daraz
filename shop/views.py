from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product, Category, Offer
from .forms import ProductForm, CategoryForm, OfferForm


def home(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    
    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()
    
   
    offers = Offer.objects.filter(is_active=True)

    return render(request, 'shop/home.html', {
        'products': products, 
        'categories': categories,
        'offers': offers
    })

def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    
    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()

    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    offers = Offer.objects.all()
    return render(request, 'shop/dashboard.html', {
        'products': products, 
        'categories': categories,
        'offers': offers
    })

@login_required
@user_passes_test(superuser_required)
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect('shop:dashboard')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form, 'title': 'Create Product'})

@login_required
@user_passes_test(superuser_required)
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('shop:dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form, 'title': 'Update Product'})

@login_required
@user_passes_test(superuser_required)
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect('shop:dashboard')
    else:
        form = CategoryForm()
    return render(request, 'shop/category_form.html', {'form': form, 'title': 'Create Category'})

@login_required
@user_passes_test(superuser_required)
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('shop:dashboard')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/category_form.html', {'form': form, 'title': 'Update Category'})


@login_required
@user_passes_test(superuser_required)
def create_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'অফার created')
            return redirect('shop:dashboard')
    else:
        form = OfferForm()
    
    return render(request, 'shop/offer_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(superuser_required)
def update_offer(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated')
            return redirect('shop:dashboard')
    else:
        form = OfferForm(instance=offer)
    
    return render(request, 'shop/offer_form.html', {'form': form, 'offer': offer, 'action': 'Update'})

@login_required
@user_passes_test(superuser_required)
def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    messages.success(request, '')
    return redirect('shop:dashboard')