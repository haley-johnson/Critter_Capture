from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animal_Log, Animals
import requests
from datetime import date

API_KEY = 'VSrG5uDX/jdGVlbkMmLrDA==pW0aLq36IRlIssCj' 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import base64
from test.identify import identify as id

# View for the home page
def home(request):
    return render(request, 'test/home.html')

# View for the contact page
def critters(request):
    print("HERE")
    logs = Animal_Log.objects.all()  # Fetch all entries from the database
    logs_with_api_data = []

    for log in logs:
        response = requests.get(
            'https://api.api-ninjas.com/v1/animals',
            headers={'X-Api-Key': API_KEY},
            params={'name': log.name}
        )

        if response.status_code == 200:
            api_data = response.json()
        else:
            api_data = {"error": "Could not fetch data"}

         # Add log and API data to the list
        logs_with_api_data.append({
            "log": log,
            "api_data": api_data
        })
    print(logs_with_api_data)
    
    return render(request, 'test/critters.html', {'logs': logs})

def conservation(request):
    return render(request, 'test/conservation.html')

@csrf_exempt
def upload_image(request):
    data = json.loads(request.body)
    image_data = data.get('image_data')
    print(type(image_data))

    format, imgstr = image_data.split(';base64,')  # Split out the base64 part
    imgdata = base64.b64decode(imgstr)  # Decode the base64 string to binary data

    with open('test/static/latest.png', 'wb') as file:
        file.write(imgdata)

    print(id.identify('test/static/latest.png'))

    Animal_Log.objects.create(name=id.identify('test/static/latest.png'), date=date.today(), loc='toronto')
    return HttpResponse('200')

def critter_collection(request):
    logs = Animal_Log.objects.all()  # Fetch all entries from the database
    return render(request, 'critters.html', {'logs': logs})