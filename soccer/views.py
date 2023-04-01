from django.shortcuts import render
import requests

import datetime


from django.http import JsonResponse
# Create your views here.

def index(request):
    
    template_name = 'soccer.html'
    date_param = request.GET.get('date', None)
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"

    query_string_premier_league = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        'X-RapidAPI-Key': 'bb17079e36msh74bf5d47086ca7ep13fc06jsnc033492ad114',
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
            'date': date_param
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
        'X-RapidAPI-Key': 'bb17079e36msh74bf5d47086ca7ep13fc06jsnc033492ad114',

        "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"

        # "X-RapidAPI-Host": "livescore6.p.rapidapi.com"

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

        # Return the data as a JSON response to the frontend
        jsonResponse = JsonResponse(data, safe=False)
        # return jsonResponse

    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
    return render(request, 'soccer.html', {'jsonResponse': jsonResponse})



# def my_view(request):
    # get the date parameter from the URL query string
    date_param = request.GET.get('date', None)
    if date_param:
        # do something with the date, e.g. format it or store it in a database
        ...
    
    # render the response, e.g. a template with the processed date
    return render(request, 'my_template.html', {'date': date_param})

def fixturesByDate(request, date: str):
    template_name = 'fixtures.html'
    dt = datetime.datetime.now()
    print(dt)

    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    querystring = {"Category":"soccer","Date":date,"Timezone":"-7"}

    headers = {
        'X-RapidAPI-Key': 'bb17079e36msh74bf5d47086ca7ep13fc06jsnc033492ad114',
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

