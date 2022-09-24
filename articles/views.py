from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [
        {'name':'한식', 'price':12000}, 
        {'name':'일식', 'price':20000}, 
        {'name':'양식', 'price':20000}, 
        {'name':'분식', 'price':8000}, 
    ]

    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
    }
    return render(request, 'dinner.html', context)