from django.shortcuts import render, redirect
import pandas as pd
from requests import head
from .models import CovidPrediction
import joblib

# Create your views here.

def home(request):
    return render(request, 'home.html')

def stats(request):
    return render(request, 'stats.html')

def analysis(request):
    return render(request, 'analysis.html')

def predict(request):
    model = joblib.load('lr_model.sav')

    cough = request.GET['cough']
    fever = request.GET['fever']
    sore_throat = request.GET['sore_throat']
    shortness_breath = request.GET['shortness_breath']
    headache = request.GET['headache']
    age60 = request.GET['age60']
    contact_with_positive = request.GET['contact_with_positive']
    gender = request.GET['gender']
    abroad = request.GET['abroad']




    lis = []

    lis.append(cough)
    lis.append(fever)
    lis.append(sore_throat)
    lis.append(shortness_breath)
    lis.append(headache)
    lis.append(age60)
    lis.append(contact_with_positive)
    lis.append(gender)
    lis.append(abroad)

    print(lis)
    lis = [int(i) for i in lis]
    classification = model.predict([lis])

    CovidPrediction.objects.create(
        cough=cough,
        fever=fever,
        sore_throat=sore_throat,
        shortness_breath=shortness_breath,
        headache=headache,
        age60=age60,
        contact_with_positive=contact_with_positive,
        gender=gender,
        abroad=abroad,
        classification=classification[0]
    )

    return render(request, 'predict.html', {'classification_result': classification[0]})
