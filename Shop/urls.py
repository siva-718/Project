from django.urls import path
from . import views
app_name='Shop'
urlpatterns=[
    path('',views.allProducts,name='allProducts'),
    path("<slug:c_slug>/",views.allProducts,name='products_by_category'),
    path("<slug:c_slug>/<slug:prod_slug>/", views.prodwise, name='product_wise')
]