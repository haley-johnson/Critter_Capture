from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animal_Log, Animals
import requests

API_KEY = 'VSrG5uDX/jdGVlbkMmLrDA==pW0aLq36IRlIssCj' 

# View for the home page
def home(request):
    return render(request, 'test/home.html')

# View for the contact page
def critters(request):
    print("HERE")
    logs = Animal_Log.objects.all()  # Fetch all entries from the database
    print(logs)
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
