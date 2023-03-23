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
    
    return render(request, 'home/index-4.html', {'jsonResponse': jsonResponse})
