from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    names = ['khai', 'hoa', 'thanh', 'hieu']
    context = {"names": names}
    return render(request, 'polls/index.html', context)