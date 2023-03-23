from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def index(request):
    
    template_name = 'index.html'
    
    baseurl = "https://livescore6.p.rapidapi.com/matches/v2/"
    endpoint = "list-live"
    
    url = baseurl+endpoint
    
    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "d31ffed9cdmshdd3b46d49113fffp17b050jsn36beb1a72767",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # data = response.json()

    # stages = data['Stages'][0]
    # print(stages.keys())
    # events = stages.get('Events')


    # print(events)
    # print(events[0].keys())
    
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
        # jsonResponse = JsonResponse(data, safe=False)
        # return jsonResponse
    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
    return render(request, 'index.html', {'jsonResponse': jsonResponse})




def fixtures(request):  #by date
    
    template_name = 'index.html'
    
    baseurl = "https://livescore6.p.rapidapi.com/matches/v2/"
    endpoint = "list-by-date"
    
    url = baseurl+endpoint
    
    querystring = {"Category":"soccer", "Date":"20201028", "Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "d31ffed9cdmshdd3b46d49113fffp17b050jsn36beb1a72767",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


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
    
    return render(request, 'index.html', {'jsonResponse': jsonResponse})







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
