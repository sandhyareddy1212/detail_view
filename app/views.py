from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView


# Create your views here.
from app.models import *



class SchoolList(ListView):
    model=School
    context_object_name='allSO'

class SchoolDetail(DetailView): 
    model=School
    context_object_name='DOSI'   
