from .models import Mapclient
from .models import Bolnichnyepalaty
from .models import Spisokperiodov
from django.shortcuts import render

def index(request):
     bbx = Spisokperiodov.objects.all()
     return render(request, "btest/index.html", {'bbx': bbx})
     
