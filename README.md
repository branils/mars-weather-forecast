# Mars Weather Forecast
small student project of network and bus technology course 


# Links
* [NASA Weather Forecast](https://mars.nasa.gov/insight/weather/) 
* [Wikipedia Article of Mars InSight Mission](https://en.wikipedia.org/wiki/InSight) abzufragen, zu verarbeiten und auf einem kleinen Display anzuzeigen.
* [NASA API](https://api.nasa.gov)
## Topology of the Project  

![Topology](/Misc/topology.png)

## Hardware 
### [Raspberry Pi 3 Model B Plus Rev 1.3](https://www.unixtutorial.org/command-to-confirm-raspberry-pi-model)

### Display (LCD) 
[Hitachi HD44780](https://cdn-shop.adafruit.com/datasheets/HD44780.pdf)
[LCD Module 1602A-1](https://www.openhacks.com/uploadsproductos/eone-1602a1.pdf)

# Software
Language: **Python**

## Communication between NASA API and Raspberry Pi

### NASA-API
Generate API Key ([api.nasa.gov](https://api.nasa.gov)) for authentification. Study the [InSight documentation](https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf) for desired values.  

final URL: `https://api.nasa.gov/insight_weather/?api_key=<YOUR_API-KEY>&feedtype=json&ver=1.0`
(for testing reasons you can simply use this demo URL: [https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0](https: //api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0)

### Python HTTP-Requests
* **requests** library (`pip install requests`).
* implementation: [request_nasa.py](/src/request_nasa.py)
![nested json data](/Misc/nested_json_data.png)

## Display communication
[lcd.py](/src/lcd.py) 

# Result

![Average Wind speed](/Misc/av_Wind_speed.jpg)
![Average Temperature](/Misc/av_Temp.jpg)
