from django.shortcuts import render

def index(request):
    # Sample product data
    products = [
        {'name': 'Tomato', 'price': 30, 'farmer': 'Naveen', 'desc': 'Fresh organic tomatoes'},
        {'name': 'Rice', 'price': 60, 'farmer': 'Aravind', 'desc': 'Premium quality rice'},
        {'name': 'Banana', 'price': 50, 'farmer': 'Selvaa', 'desc': 'Sweet bananas from local farm'}
    ]
    return render(request, 'index.html', {'products': products})

# store/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Order
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

@login_required
def farmer_dashboard(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['description']
        product = Product.objects.create(
            name=name, price=price, description=desc,
            farmer=request.user
        )
        return redirect('farmer_dashboard')
    my_products = Product.objects.filter(farmer=request.user)
    return render(request, 'farmer_dashboard.html', {'my_products': my_products})

@login_required
def buy_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        qty = int(request.POST['quantity'])
        Order.objects.create(product=product, customer=request.user, quantity=qty)
        return render(request, 'buy.html', {'product': product, 'message': 'Order placed!'})
    return render(request, 'buy.html', {'product': product})
@login_required
def farmer_dashboard(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['description']
        image = request.FILES.get('image')
        Product.objects.create(
            name=name, price=price, description=desc,
            farmer=request.user, image=image
        )
        return redirect('farmer_dashboard')
    my_products = Product.objects.filter(farmer=request.user)
    return render(request, 'farmer_dashboard.html', {'my_products': my_products})
