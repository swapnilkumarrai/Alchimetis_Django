from django.shortcuts import render, HttpResponse
import pandas as pd
import numpy as np
from Alchimetis_app.models import Report
import math

# Create your views here.

# def read_data(request):
#     df = pd.read_csv('grid_data_2023Sep13_10h29m3s.csv')
#     for i in range(df.shape[0]):
#         a = list(df.loc[i])
#         for j in range (len(a)):
#             if isinstance(a[j], (float, int)) and math.isnan(a[j]):
#                 a[j] = None
#             elif isinstance(a[j], str) and a[j].lower() == 'nan':
#                 a[j] = None
#             else:
#                 print('')
#         ins = Report(Scope=a[0], Category=a[1], DataType=a[2], Location=a[3], TotalData=a[4], Emissions_t_of_CO2e=a[5], Scope_3_Indirect_Emissions=a[6], LifecycleEmissions=a[7], Floor_space_m2=a[8], EmissionsIntensity=a[9], CO2Emissions=a[10], CH4Emissions=a[11], N2OEmissions=a[12])
#         ins.save()

#     return HttpResponse('200 - Success')


def display_data(request):
    alldata = Report.objects.all()
    context = {'reports':alldata}
    return render(request, 'index.html', context)