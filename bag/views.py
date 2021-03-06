from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """A view to return the shopping bag"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a item to the shopping bag with quantity"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.warning(request, f'Removed {product.name} to your shopping bag')

    request.session['bag'] = bag
    return HttpResponse(status=200)
