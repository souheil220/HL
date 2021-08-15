from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Camion
import json

# Create your views here.

def index(request):
    camions = Camion.objects.all()
    context = {"camions":camions}
    return render(
        request,
        'camionremorque/index.html',context
    )

def modifierCamion(request):
    return render(
        request,
        'camionremorque/modifier_camion.html'
    )

def loadMore(request,name):
    if request.is_ajax and request.method == "GET":
        result = Camion.objects.filter(matriculation__icontains=name)[:5]
        data = {}
        i = 0
        for camion in result:
            data[i] = {}
            data[i]['id'] = camion.id
            data[i]['matriculation'] = camion.matriculation
            data[i]['remorque'] = camion.remorque.matriculation
            data[i]['matriculation'] = camion.matriculation
            i = i+1
        return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")
    else:
        raise Http404