from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_customers=Customer.objects.all().order_by('-date')
    return render(request, 'index.html',{'all_customers': all_customers})

def customer(request, id):
    single_customer=Customer.objects.get(id=id)
    return render(request, 'customer.html', {'single_customer': single_customer})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')

def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone= request.POST['phone']
        
        form = Customer(first_name=first_name, second_name=second_name, last_name=last_name, email=email, phone=phone)
        form.save()
        messages.success(request, 'Customer successfully added')
        return redirect('index')
    return render(request, 'add.html')

def edit(request, id):
    single_customer= Customer.objects.get(id=id)
    form = CustomerForm(instance=single_customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=single_customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer successfully updated')
            return redirect('index')
    return render(request, 'edit.html', {'form': form})


def remove(request, id):
    single_customer = Customer.objects.get(id=id)
    single_customer.delete()
    return redirect('/')
