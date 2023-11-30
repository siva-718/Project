from django.urls import path
from . import views
urlpatterns=[
    path('',views.LIstView.as_view(),name='home'),
    path('delete/<int:pk>/',views.deleteview.as_view(),name='delete'),
    path('update/<int:pk>/',views.updateview.as_view(),name='update'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detail'),
]