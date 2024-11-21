from django.shortcuts import render
# from app1.models import register

# Create your views here.
def index(request):
    return render(request,"index.html")