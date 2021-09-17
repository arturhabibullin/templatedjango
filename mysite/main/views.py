from main.models import Sample
from django.shortcuts import render

# Create your views here.
def samples_list(request):
    samples = Sample.objects.all()
    context = {
        'samples':samples
    }
    return render(request, 'main/samples_list.html', context)
