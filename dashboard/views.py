from django.shortcuts import render, redirect, get_object_or_404
from .forms import Creatuserform, Customerform,Categorietypeform
from .models import Customer,Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pytz
import datetime
from django.utils.timezone import utc



# Create your views here.
def register_view(request):
    form = Creatuserform(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account is created for {username}')
        Customer.objects.create(user=user)
        return redirect('/login')
    context = {'form': form}
    return render(request, "register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')

    return render(request, "login.html", )


def logout_view(request):
    logout(request)
    return redirect("/login")


@login_required(login_url='login')

def home_view(request, *args, **kwargs):

    # queryset2 = request.user.customer
    # print('object_list2:', queryset2)

    # context = {

    # "object_list2": queryset2,
    # }

    return render(request, "home.html")


@login_required(login_url='login')





def accountsettings_view(request, *args, **kwargs):
    customer = request.user.customer
    form = Customerform(instance=customer)
    if request.method == 'POST':
        form = Customerform(request.POST, request.FILES, instance=customer)
        form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, "account_settings.html", context)




    





'''
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)
'''

@login_required(login_url='login')
def categories_view(request):
    # queryset = Categorietype.objects.all()
    queryset = request.user.post_set.all()

    context = {

        "object_list": queryset,
    }

    return render(request, "categories.html", context, )
@login_required(login_url='login')
def editcategories_view(request):
    form = Categorietypeform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/categories')
    context = {
        'form': form,
    }

    return render(request, "ppp.html", context)
@login_required(login_url='login')
def updatecategories_view(request, pk):
    ins = Post.objects.get(id=pk)
    form = Categorietypeform(instance=ins)
    if request.method == "POST":
        form = Categorietypeform(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            return redirect('/categories')
    context = {
        'form': form,
    }

    return render(request, "ppp.html", context)
#############################################################

