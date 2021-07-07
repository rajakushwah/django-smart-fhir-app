from django.shortcuts import render
import request
# Create your views here.

def first(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/first.html', param)


def main(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/main.html', param)


def index(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/index.html', param)

