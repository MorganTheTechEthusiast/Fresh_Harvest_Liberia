from django.shortcuts import render

# Create your views here.

def home(request):
    page_title = "Home - Fresh Harvest Liberia"
    context = {
        'page_title': page_title,
    }
    return render(request, 'home.html', context)


def shop(request):
    page_title = "Shop - Fresh Harvest Liberia"

    context = {
        'page_title': page_title,
    }
    return render(request, 'products/products.html', context)

def product_detail(request):
    page_title = "Product Details - Fresh Harvest Liberia"
    
    context = {
        'page_title': page_title,
    }
    return render(request, 'products/product_details.html', context)

def cart(request):
    page_title = "Shopping Cart - Fresh Harvest Liberia"

    context = {
        'page_title': page_title,
    }
    return render(request, 'products/cart.html', context)

def checkout(request):
    page_title = "Checkout - Fresh Harvest Liberia"

    context = {
        'page_title': page_title,
    }
    return render(request, 'checkout.html', context)

def contact(request):
    page_title = "Contact Us - Fresh Harvest Liberia"
    context = {
        'page_title': page_title,
    }
    return render(request, 'contact.html', context)