from django.shortcuts import render
import requests

import datetime

from django.http import JsonResponse
# Create your views here.

def index(request):
    dt = datetime.datetime.now()
    Fixtures = []
    template_name = 'soccer.html'
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string_premier_league = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=query_string_premier_league)

    
    # Check if the API call was successful
    if response.status_code == 200:
        # Convert the response content to JSON
        data = response.json()
        
        stages = data['Stages']
        
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
                
        print('Fixtures', Fixtures)
        context = {
            'stages':stages,
            'fixtures':Fixtures[0:25],
        }
        return render(request, template_name, context)
        # Return the data as a JSON response to the frontend
    else:
        # If the API call failed, return the error message as a JSON response
        print('failed')
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    




def league_events(request, country: str, league: str):
    Results = []
    Fixtures = []
    template_name = 'leagues.html'
    
    dt = datetime.datetime.now()
    print(dt.strftime('%Y-%m-%d'))
    datefmt = str(dt.year)+str(dt.month)+str(dt.day)
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string = {"Category":"soccer","Ccd":country,"Scd":league,"Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=query_string)
    
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
                
                if event_year < dt.year:
                    Results.append(row)
                elif event_year == dt.year and event_month < dt.month:
                    Results.append(row)
                elif event_year == dt.year and event_month == dt.month:
                    if event_day < dt.day:
                        Results.append(row)
                    else:
                        Fixtures.append(row) 
                elif  event_year >= dt.year and event_month > dt.month:
                    Fixtures.append(row)
                    
        print('Fixtures', len(Fixtures))
        print('Results', len(Results))

        context={
            'stages':stages,
            'Fixtures':Fixtures,
            'Results':Results,
            'Competion_name':competion_name,
        }
    else:
        context={
            'Fixtures':Fixtures,
            'Results':Results,
            'Competion_name':"Null",
        }
    return render(request, template_name, context)


def live(request):

    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    
    template_name = 'live.html'
    print(response.status_code)
    # Check if the API call was successful
    if response.status_code == 200:
        # Convert the response content to JSON
        data = response.json()

        
        stages = data['Stages']
        
        context = {
            'stages':stages,
        }
        return render(request, template_name, context)

        # Return the data as a JSON response to the frontend
        jsonResponse = JsonResponse(data, safe=False)
        # return jsonResponse

    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
   

def fixturesByDate(request, date: str):
    template_name = 'fixtures.html'
    dt = datetime.datetime.now()
    print(dt.strftime('%Y-%m-%d'))
    datefmt = str(dt.year)+str(dt.month)+str(dt.day)
    
    if request.method == 'POST':
        live_date = request.POST['date']
        print(live_date, 'live_date')
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    querystring = {"Category":"soccer","Date":date,"Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    stages = data['Stages']            
    
    # for stage in stages:
    #     # ids = stage.Sid
    #     name = stage.CompN
    #     desc = stage.CompD
        
        # print(ids, name, desc)
        
        
    context = {
        'stages':stages,
        'today': dt.strftime('%Y-%m-%d'),
       
    }
    
    return render(request, template_name, context)

# def get_livescore(request):
#     # Replace with your LiveScore API endpoint URL and API key
#     endpoint = 'https://livescore-api.com/api-client/scores/live.json'
#     api_key = 'YOUR_API_KEY'

#     # Set optional parameters for the API call
#     params = {
#         'key': api_key,
#         'secret': 'YOUR_API_SECRET',
#         'countries': 'england',
#         'leagues': 'premier-league',
#         'timezone': 'Europe/London'
#     }

#     # Make a GET request to the API endpoint using requests library
#     response = requests.get(endpoint, params=params)
    
#     # Check if the API call was successful
#     if response.status_code == 200:
#         # Convert the response content to JSON
#         data = response.json()
#         # Return the data as a JSON response to the frontend
#         return JsonResponse(data)
#     else:
#         # If the API call failed, return the error message as a JSON response
#         error_message = {'error': response.reason}
#         return JsonResponse(error_message, status=response.status_code)

