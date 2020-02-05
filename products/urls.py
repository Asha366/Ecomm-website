from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="asha"),
    path('create/',views.index,name="kumari"),
    path('men/',views.men,name="thakur"),
    path('kids/',views.child,name="kids")
]