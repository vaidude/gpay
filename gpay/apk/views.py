from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def indx(request):
    return render(request,'index.html')
@login_required(login_url="/accounts/login/")
def home(request):
    return render(request,'home.html')

def cregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST['password']
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')

        if name and email and phone and photo:
            customer = Customer(name=name, email=email, password=password, phone=phone, photo=photo)
            customer.save()
            messages.success(request, 'Login successful!')
            return redirect('clogin')
    
    return render(request, 'register.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customerlist.html', {'customers': customers})

from django.contrib.auth import authenticate, login
from django.contrib import messages

def clogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            request.session['customer_id'] = customer.id
            request.session['email'] = customer.email
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to customer dashboard upon successful login
        except Customer.DoesNotExist:
            message = 'Login failed. Invalid email or password.'
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('clogin')