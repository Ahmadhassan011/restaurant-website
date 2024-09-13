from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import home_images, Appetizers, Main_course, Dessert, Chef, Message
# Create your views here.

def home(request):
    n = request.GET.get('n', '')
    items_dict = {
        'mains': Appetizers.objects.all(),
        'mains01': Main_course.objects.all(),
        'mains02': Dessert.objects.all(),
        'mains03': Chef.objects.all(),
        'main_images': home_images.objects.all(),
        'n' : n
    }

    return render(request, "home.html", items_dict)

def contact(request):
    n = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        res = Message(name=name, email=email, message=message)
        res.save()
    n = 'Message sent Successfully'
    return redirect(f'/?n={n}')