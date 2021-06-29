from django.shortcuts import render
import request
# Create your views here.
def home(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/home.html', param)
