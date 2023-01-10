from django.shortcuts import render
import requests
import os
import pandas as pd
import my_function


def index(request):
    return render(request, 'index.html')


