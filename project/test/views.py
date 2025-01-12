from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animal_Log, Animals

# View for the home page
def home(request):
    return render(request, 'test/home.html')

# View for the contact page
def critters(request):
    return render(request, 'test/critters.html')

def conservation(request):
    return render(request, 'test/conservation.html')

def critter_collection(request):
    logs = Animal_Log.objects.all().values() # Fetch all entries from the database
    template = loader.get_template('critters.html')
    context = {'logs': logs}
    return HttpResponse(template.render(context, request))
    #return render(request, 'critters.html', {'logs': logs})