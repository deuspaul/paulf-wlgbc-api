<h1 align="center">
  <br>
 <img src="https://github.com/deuspaul/paulf-wlgbc-api/blob/main/media/weatherStatusAPIlogo.PNG" alt="WeatherStatus API">
  <br>
  Weather Status API
  <br>
</h1>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#how-to-run">How To Run</a> •
  <a href="#unit-tests">Unit Test</a> •
  <a href="#live-demo">Live Demo</a> •
</p>
  <br>


## Description
Simple API Application for the Wizeline Golang Bootcamp



  <br><br>
## How To Run<br>

To clone and run this application, you'll need [Git](https://git-scm.com), python3.6+(https://nodejs.org/en/download/), python3-pip and flask 1.1.2+ installed on your computer. You will also need to register and obtain an API key from: https://openweathermap.org/api

From your command line run:

```bash
# Clone this repository
$ git clone https://github.com/deuspaul/paulf-wlgbc-api.git

# Go into the repository
$ cd paulf-wlgbc-api

# Create the file with the API Key
$ touch cred_wlgbc.py
apiKey = "<your api key>"

# Install required packages
$ pip3 install -r requirements.txt 

# Run the app
$ export FLASK_APP=main.py
$ flask run
```


  <br><br>
## Unit Tests<br>

<img src="https://github.com/deuspaul/paulf-wlgbc-api/blob/main/media/UnitTest.PNG" alt="UnitTest">


```bash
# Run the unit tests
$ python3 -m unittest test_main.py
```

  <br><br>
## Live Demo<br>
Test Hello World endpoint: http://52.224.64.102:5000/
Test get_weather api endpoint: http://52.224.64.102:5000/weather/<city name> for example: http://52.224.64.102:5000/weather/guadalajara
