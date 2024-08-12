from django.shortcuts import render
from movieForms.models import Project
from movieForms.forms import ProjectForms

# Create your views here.

def index(request):
    return render(request,'movieForms/index.html')

def listMovies(request):
    moviesList = Project.objects.all()
    return render(request,'movieForms/listMovies.html',{'movies':moviesList})

def addMovies(request):
    form = ProjectForms()
    if request.method == "POST":
        form = ProjectForms(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'movieForms/addMovie.html',{'form':form})





