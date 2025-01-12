from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animal_Log, Animals
import requests
from datetime import datetime

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
    logs = Animal_Log.objects.all().order_by('-date')  # Fetch all entries from the database
    #print(logs)
    #logs_with_api_data = []

    # for log in logs:
    #     response = requests.get(
    #         'https://api.api-ninjas.com/v1/animals',
    #         headers={'X-Api-Key': API_KEY},
    #         params={'name': log.name}
    #     )

    #     if response.status_code == 200:
    #         api_data = response.json()
    #     else:
    #         api_data = {"error": "Could not fetch data"}

    #      # Add log and API data to the list
    #     logs_with_api_data.append({
    #         "log": log,
    #         "api_data": api_data
    #     })
    #print(logs_with_api_data)

    endangerment_mapping = {
        "dog": "least-concern",
        "sheep": "least-concern",
        "fox": "vulnerable",
        "dog": "least-concern",
        "housecat": "least-concern",
        "spider": "least-concern",
        "horse": "least-concern",
        "elephant": "endangered",
        "squirrel": "least-concern",
        "chicken": "least-concern",
        "butterfly": "least-concern",
        "boar": "least-concern",
        "bird": "least-concern",
        "deer": "vulnerable"
    }

    log_with_endangerment_level = []
    for log in logs:
        log_with_endangerment_level.append({
            'name': log.name.capitalize(),
            'date': log.date,
            'class_name': endangerment_mapping.get(log.name.lower(), "neutral")
        })
    #print(log_with_endangerment_level)
    
    return render(request, 'test/critters.html', {'logs': log_with_endangerment_level})

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

    Animal_Log.objects.create(name=id.identify('test/static/latest.png'), date=datetime.now(), loc='toronto')
    return HttpResponse('200')

def critter_collection(request):
    logs = Animal_Log.objects.all()  # Fetch all entries from the database
    return render(request, 'critters.html', {'logs': logs})