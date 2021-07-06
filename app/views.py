from django.shortcuts import render
# Create your views here.
def home(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/homenew.html', param)


def main(request):
    param = {'param': "THIS IS SAMPLE APP"}
    return render(request, 'app/index.html', param)
