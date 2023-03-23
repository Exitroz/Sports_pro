from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def index(request):
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "bb17079e36msh74bf5d47086ca7ep13fc06jsnc033492ad114",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    
    # Check if the API call was successful
    if response.status_code == 200:
        # Convert the response content to JSON
        data = response.json()
        # Return the data as a JSON response to the frontend
        jsonResponse = JsonResponse(data, safe=False)
        # return jsonResponse
    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    
    return render(request, 'soccer.html', {'jsonResponse': jsonResponse})



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
