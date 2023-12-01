from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Movie
from .forms import Movieform
# Create your views here.
def home(request):
    mov=Movie.objects.all()
    context={
        'movies':mov
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mov':movie})
def add(request):
    if request.method=='POST':
        name= request.POST.get('Name')
        desc = request.POST.get('Desc')
        year = request.POST.get('Year')
        img = request.FILES['Img']
        movie= Movie(Name=name, Desc=desc, Year=year,Img=img)
        movie.save()
    return render(request,'Add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'UPDATE.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')