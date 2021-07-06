from django.shortcuts import render
# import request
# Create your views here.
def main(request):
    return render(request, 'app/index.html', param)
