from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
import joblib
from django.contrib import messages
from keras import backend as K

# Create your views here.

class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


def ohe_value(df):
    ohe_col = joblib.load('MyAPI/OHE_cols.pkl')
    cat_variables = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    processed_df = pd.get_dummies(df, columns = cat_variables)
    new_dict = {}
    for i in ohe_col:
        if i in processed_df.columns:
            new_dict[i] = processed_df[i].values
        else:
            new_dict[i] = 0

    newdf = pd.DataFrame(new_dict)
    return newdf




# @api_view(['POST'])
def approveReject(unit):
    try:
        mdl = joblib.load('MyAPI/loan_model.pkl')
        scalers = joblib.load('MyAPI/scalers.pkl')
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred>0.58)
        new_df = pd.DataFrame(y_pred, columns=['Status'])
        new_df = new_df.replace({True: 'Approved', False: 'Rejected'})
        K.clear_session()
        return (new_df.values[0][0])
    except (TypeError,ValueError) as e:
        return (e.args)

def cxcontact(request):
    if request.method =='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            Dependents = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
            # print(firstname, lastname, dependents,married, area)
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approveReject(ohe_value(df))
            if int(df['LoanAmount']) < 25000:
                messages.success(request, 'Application Status: {}'.format(answer))
            else:
                messages.success(request, 'Invalid: Your Loan Amount Exceeds $25000 Limit')
            # print(ohe_value(df))

    form = ApprovalForm()

    return render(request, 'myform/cxform.htm', {'form': form})