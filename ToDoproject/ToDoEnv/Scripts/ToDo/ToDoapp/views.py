from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TODO
from .forms import ToDoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView
# Create your views here.
# def home(request):
#     obj=TODO.objects.all()
#     if request.method=='POST':
#         name= request.POST.get('Task','')
#         prio = request.POST.get('Priority','')
#         date=request.POST.get('Date','')
#         todo=TODO(Task=name,Priority=prio,Date=date)
#         todo.save()
#
#     return render(request,'home.html',{'vb':obj})
# def delete(request,tid):
#     tk=TODO.objects.get(id=tid)
#     if request.method =='POST':
#         tk.delete()
#         return redirect('/')
#     return render(request,'delete.html')
# def update(request,id):
#     ob=TODO.objects.get(id=id)
#     f=ToDoForm(request.POST or None, instance=ob )
#     if f.is_valid():
#         f.save()
#         return redirect('/')
#     return render(request,'update.html',{'f':f,'ob':ob})
class LIstView(ListView):
    model = TODO
    template_name = 'home.html'
    context_object_name = 'vb'
class detailview(DetailView):
    model = TODO
    template_name = 'detail.html'
    context_object_name = 'dt'
class deleteview(DeleteView):
    model = TODO
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
class updateview(UpdateView):
    model = TODO
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    context_object_name = 'up'
    fields = {'Task','Priority','Date'}