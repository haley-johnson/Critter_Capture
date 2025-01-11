from django.shortcuts import render

# View for the home page
def home(request):
    return render(request, 'test/home.html')

# View for the contact page
def critters(request):
    return render(request, 'test/critters.html')