import requests
import json
from pprint import pprint as pp
from json import JSONDecodeError
import time

class Town:
    def __init__(self,name,lat,lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.getData()
    
    def getData(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=?'
        parmateres = {'APPID': '#YOUR OWN API ID', 'q': 'Piscataway,NJ,US'}
        r = requests.get(url, params= parmateres)

        #PRinting the data for Piscataway< New Jersey
        print("The Requested data via API of Piscataway, NJ is: ")
        dataobj = r.json()
        time.sleep(1)
        print(json.dumps(dataobj, indent= 4))
        print()
        
        print("The keys of the Requested API are:")
        time.sleep(1)
        pp(((list(dataobj.keys()))))
        print()

        try:
            self.name = dataobj['name']
        except JSONDecodeError as error:
            print("JSON DATA decoding error:")
            print(error.msg)
            print("The error line number is : ", error.lineno)
            print("The column number is:", error.colno)

        try:
            self.temp = dataobj['main']['temp']
        except JSONDecodeError as error1:
            print("JSON DATA decoding error:")
            print(error1.msg)
            print("The error line number is : ", error1.lineno)
            print("The column number is:", error1.colno)

        try:
            self.visibilty = dataobj['visibility']
        except JSONDecodeError as error2:
            print("JSON DATA decoding error:")
            print(error2.msg)
            print("The error line number is : ", error2.lineno)
            print("The column number is:", error2.colno)

        try:
            self.country = dataobj['sys']['country']
        except JSONDecodeError as error3:
            print("JSON DATA decoding error:")
            print(error3.msg)
            print("The error line number is : ", error3.lineno)
            print("The column number is:", error3.colno)

        try:
            self.timezone = dataobj['timezone']
        except JSONDecodeError as error4:
            print("JSON DATA decoding error:")
            print(error4.msg)
            print("The error line number is : ", error4.lineno)
            print("The column number is:", error4.colno)
    
        try: 
            self.weather = dataobj['weather']
        except JSONDecodeError as error5:
            print("JSON DATA decoding error:")
            print(error5.msg)
            print("The error line number is : ", error5.lineno)
            print("The column number is:", error5.colno)
       
    def printing_all_the_values(self):
        units = 'F'

        print(f"The name of the town is : {self.name}")
        time.sleep(1)
        print()

        print(f"Piscataway is in which country?: {self.country}")
        time.sleep(1)
        print()

        print(f"The timezone of Piscataway is: {self.timezone}")
        time.sleep(1)
        print()

        print(f"The Temperature in Piscataway,NJ is: {self.temp} {units}")
        time.sleep(1)
        print()
        
        print(f"The visibilty in Piscataway,NJ is: {self.visibilty}")
        time.sleep(1)
        print()

        print(f"The weather in Piscataway is: {self.weather}")
        time.sleep(1)
        print()


my_town = Town("Piscataway,NJ", 40.5549, 74.4643)
my_town.printing_all_the_values()
