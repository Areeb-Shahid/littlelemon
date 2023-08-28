from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from demoapp.forms import BookingForm
from .models import Menu

    
def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)


def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")  

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all()
    context = {'menu': menu_items}

    return render(request, 'menu.html', context)

def menu_item_detail(request, item_id):
    item = get_object_or_404(Menu, pk=item_id)
    return render(request, 'menu_item.html', {'item': item})

def book(request):
    return render(request, 'book.html')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(f"{date_joined}")