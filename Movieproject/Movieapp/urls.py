from django.urls import path
from . import views
app_name='Movieapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add, name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name ='delete'),
]