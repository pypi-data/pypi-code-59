import requests

def add_numbers(num1,num2):
    return num1+num2

def subtract_numbers(num1,num2):
    return num1-num2

def multiply_numbers(num1,num2):
    return num1*num2

def divide_numbers(num1,num2):
    return num1/num2

def power_numbers(num1,power):
    return num1 ** power

def total_numbers(*args):
    x = 0
    for i in range(len(args)):
        x += args[i]
    return x

class check_weather:
    def __init__(self, city_name, api_key="", unit="metric"):
        self.dump_api_key = 'f17085e5d81ef9246425b66f31b34489'
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}"
        if(api_key == ""):
            self.data_appid = self.dump_api_key
        else:
            self.data_appid = api_key
        self.data_city = city_name
        self.data_unit = unit
        
    def seaching_weather_data(self):
        weather_data_c = []
        r = requests.get(self.url.format(self.data_city,self.data_unit,self.data_appid)).json()

        city_weather = {
            'city': r['name'],
            'longitude': r['coord']['lon'],
            'latitude': r['coord']['lat'],
            'units': self.data_unit,
            'temperature': r['main']['temp'],
            'feel': r['main']['feels_like'],
            'min': r['main']['temp_min'],
            'max': r['main']['temp_max'],
            'pressure': r['main']['pressure'],
            'humidity': r['main']['humidity'],
            'visibility': r['visibility'],
            'windSpeed': r['wind']['speed'],
            'windDeg': r['wind']['deg'],
            'country':r['sys']['country'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data_c.append(city_weather)
        return weather_data_c

