from django.shortcuts import render
import requests

import datetime


from django.http import JsonResponse
# Create your views here.



def index(request):    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-league"
    
    querystring = {"Category":"soccer","Ccd":"england","Scd":"premier-league","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "6b988f2637msh4473b4fe6cd4359p151307jsn6639db590b7a",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request('GET', url, headers=headers, params=querystring)

    
    # response = requests.get(url, headers=headers, params=querystring)
    print(response.status_code)

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

        
        stages = data['Stages']
        
        # for stage in stages:
        #     print(stage.keys())
            
        #     table = stage['LeagueTable']['L'][0]['Tables']
            
        #     for row in table:
        #         print(row.keys())
        #         print(row.values())
            
        context = {
            'stages':stages,
        }
        
        return render(request, 'home/index.html', context)


        # Return the data as a JSON response to the frontend
        jsonResponse = JsonResponse(data, safe=False)
        # return jsonResponse

    else:
        # If the API call failed, return the error message as a JSON response
        error_message = {'error': response.reason}
        return JsonResponse(error_message, status=response.status_code)
    

    return render(request, 'home/index.html', {'jsonResponse': jsonResponse})

    return render(request, 'home/index-4.html', {'jsonResponse': jsonResponse})

