from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def demo(request):
    object = Place.objects.all()
    item= Team.objects.all()
    return render(request, "index.html",{'result':object,'res':item})



