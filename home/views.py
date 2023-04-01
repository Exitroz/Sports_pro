
from django.shortcuts import render
import requests
import datetime
from django.http import JsonResponse
# Create your views here.


def index(request):  
    dt = datetime.datetime.now()
    Fixtures = []  
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"
    
    querystring = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request('GET', url, headers=headers, params=querystring)

    
    # response = requests.get(url, headers=headers, params=querystring)
    print(response.status_code)
    # Check if the API call was successful
    if response.status_code == 200:
        # Convert the response content to JSON
        data = response.json()
        
        stages = data['Stages']
        
        for stage in stages:
            # print(stage.keys())
            competion_name = stage['CompN']
            events = stage['Events']
            print('events', len(events))
            for row in events:
                # print(row.keys())
                # print(row['Esd'])
                event_date = row['Esd']
                event_year = int(str(event_date)[0:4])
                event_month = int(str(event_date)[4:6])
                event_day = int(str(event_date)[6:8])
                # print(event_year, 'ED',event_day, 'DTD',dt.day, 'EM',event_month, 'DTM',dt.month)
                
                if  event_year >= dt.year and event_month == dt.month:
                    if not event_day < dt.day:
                        Fixtures.append(row)
                elif event_year >= dt.year and event_month > dt.month:
                    Fixtures.append(row)
            
        context = {
            'stages':stages,
            'fixtures':Fixtures[0:25],
        }
        
        return render(request, 'home/index.html', context)

    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
    return render(request, 'home/index.html', {'jsonResponse': jsonResponse})

