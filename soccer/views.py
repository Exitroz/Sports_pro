
from django.shortcuts import render
import requests
import datetime
from django.conf import settings


from django.http import JsonResponse
# Create your views here.

def index(request):
    dt = datetime.datetime.now()
    Fixtures = []
    template_name = 'soccer.html'
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string_premier_league = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=query_string_premier_league)

    
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
                
        # print('Fixtures', Fixtures)
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
    

def competion_events(request, league: str, stage: str):
    Results = []
    Fixtures = []
    template_name = 'competions.html'
    
    dt = datetime.datetime.now()
    print(dt.strftime('%Y-%m-%d'))
    datefmt = str(dt.year)+str(dt.month)+str(dt.day)
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string = {"Category":"soccer","Ccd":league,"Scd":stage,"Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
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
            stage_name = stage['Snm']
            events = stage['Events']
            # print('events', len(events))
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
                    
        # print('Fixtures', len(Fixtures))
        # print('Results', len(Results))

        context={
            'stages':stages,
            'Fixtures':reversed(Fixtures),
            'Results':reversed(Results),
            'Competion_name':competion_name,
            'stage_name':stage_name,
        }
    else:
        context={
            'Fixtures':reversed(Fixtures),
            'Results':reversed(Results),
            'Competion_name':"Null",
            'stage_name':"Null",
        }
    return render(request, template_name, context)


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
        "X-RapidAPI-Key": settings.API_KEY,
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
            try:
                competion_name = stage['CompN']
            except:
                competion_name = stage['Snm']
                
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
                    
        # print('Fixtures', len(Fixtures))
        # print('Results', len(Results))
        
        context={
            'stages':stages,
            'Fixtures':reversed(Fixtures),
            'Results':reversed(Results),
            'Competion_name':competion_name,
        }
    else:
        context={
            'Fixtures':reversed(Fixtures),
            'Results':reversed(Results),
            'Competion_name':"Null",
        }
    return render(request, template_name, context)


def live(request):
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
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
    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
    return render(request, 'soccer.html', {'jsonResponse': jsonResponse})


def single_result(request, Eid: int):
    template_name = "single-result.html"
    print("EID", Eid)
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/get-statistics"
    board_url = "https://livescore6.p.rapidapi.com/matches/v2/get-scoreboard"
    info_url = "https://livescore6.p.rapidapi.com/matches/v2/get-info"
    
    querystring = {"Category":"soccer","Eid":Eid}
    
    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    board_response = requests.get(board_url, headers=headers, params=querystring)
    info_response = requests.get(info_url, headers=headers, params=querystring)
    
    data = response.json()
    stat = data['Stat']
    try:
        pstat = data['PStat']
    except:
        pstat = []
    
    b_data = board_response.json()
    print(b_data['Incs-s'])
    
    info_data = info_response.json()
    
    context = {
        'info_data':info_data,
        'stat':stat,
        'pstat':pstat,
        'b_data':b_data,
        'incs_s':b_data['Incs-s'],
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
