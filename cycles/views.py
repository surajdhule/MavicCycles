from django.shortcuts import render
from .models import Cycle, Category, Description, Price
# Create your views here.


def cycle_store(request):
    cycles = Cycle.objects.all()
    categories = Category.objects.all()
    context = {'cycles': cycles, 'categories': categories}
    return render(request, 'cycles/homepage.html', context)


def cycle_details(request, myid):
    context = {}
    return render(request, 'cycles/bikedetails.html', context)