from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.
def aptitudes(request):
    return render(request, 'aptitudes.html')