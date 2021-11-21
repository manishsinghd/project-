from django.shortcuts import render, redirect, get_object_or_404
from .forms import Productform
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def poroducts_view(request, *args, **kwargs):
    queryset2 = Product.objects.using('products_db').all()
    print('object_list2:', queryset2)

    context = {

        "object_list2": queryset2,
    }
    return render(request, "products.html", context)
@login_required(login_url='login')
def editproduct_view(request):
    form2 = Productform(request.POST or None)
    if form2.is_valid():
        instance = form2.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/products')
    context = {
        'form2': form2,
    }

    return render(request, "2ppp.html", context)

@login_required(login_url='login')
def updateproduct_view(request, pk):
    ins1 = Product.objects.using('products_db').get(id=pk)
    form2 = Productform(instance=ins1)
    if request.method == "POST":
        form2 = Productform(request.POST, instance=ins1)
        if form2.is_valid():
            form2.save()
            return redirect('/products')
    context = {
        'form2': form2,
    }
    return render(request, "2ppp.html", context)

