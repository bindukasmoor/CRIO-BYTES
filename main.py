# coding: utf-8
# Your code here!

# Import a library that allows to make HTTP request

import requests


# Set the API endpoint

url = "https://www.metaweather.com/api/location/search/?query=bangalore"


# Use the library to perform an HTTP GET request to the URL

response = requests.get(url)


# Print out the data

if response.status_code == 200:

   #print(response.text)
    
    json_object = response.json()
    
    bglr_woeid = json_object[0]['woeid']
    #print(bglr_woeid)
    
    weather_url = "https://www.metaweather.com/api/location/%s" % bglr_woeid
    
    resp = requests.get(weather_url)
    
    if(resp.status_code == 200):
        #print(resp.text)
        weather_resp = resp.json()
        weather_state = weather_resp['consolidated_weather'][0]['weather_state_name']
        today = weather_resp['consolidated_weather'][0]['applicable_date']
        print("Weather for today dated", today, "is", weather_state);
       
    else:
        print("An Error occurred while making weather API request")
    
else:
    
    print("An Error Occurred!")
