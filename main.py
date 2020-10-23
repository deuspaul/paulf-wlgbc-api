from flask import Flask, jsonify, request
import requests, json 
import cred_wlgbc
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({"about":"Hello World"})

@app.route('/weather/<string:city>', methods=['GET'])
def get_cityweather(city):
    if type(city) != str:
        raise TypeError("please input strings only")

    # Based on the geeksforgeeks tutorial:
    #https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

    # API Key
    api_key = cred_wlgbc.apiKey
    
    # base_url variable
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
     # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
        u = x["wind"]

        # value of windspeed
        wind_speed = u["speed"]
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
        current_temperature = current_temperature - 273.15
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
    
        # print following values 
        return(" Temperature (celsius) = " +
                        str(current_temperature) +
            "\n description = " +
                        str(weather_description) +             
            "\n wind speed = " +
                        str(wind_speed) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy))           
    
    else: 
        #print(" City Not Found ") 
        return jsonify({'result':city+" not found"})

