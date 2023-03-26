from django.shortcuts import render
import requests
import datetime
from django.http import JsonResponse
# Create your views here.

def index(request):
    template_name = 'soccer.html'
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string_premier_league = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "d31ffed9cdmshdd3b46d49113fffp17b050jsn36beb1a72767",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=query_string_premier_league)
    
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
    else:
        # If the API call failed, return the error message as a JSON response
        print('failed')
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    


def live(request):
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "bb17079e36msh74bf5d47086ca7ep13fc06jsnc033492ad114",
        "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    
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



def fixturesByDate(request, date: str):
    template_name = 'fixtures.html'
    dt = datetime.datetime.now()
    print(dt)

    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    querystring = {"Category":"soccer","Date":date,"Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "d31ffed9cdmshdd3b46d49113fffp17b050jsn36beb1a72767",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    stages = data['Stages']
    
    print(response.text)
    
    context = {
        'stages':stages
    }
    
    return render(request, template_name, context)