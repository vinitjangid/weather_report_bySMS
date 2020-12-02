import requests
import json
import pyowm

hello = pyowm.OWM('a823de587ceb031a9b0c50f6b055f974')

num= int(input('Enter the mobile number: '))
city = raw_input('Enter the City name: ')
location = hello.weather_at_place(city)
weather = location.get_weather()

temp = weather.get_temperature('celsius')
hum= weather.get_humidity()
t = 'The Current temperature of '+city+ ' is ' +str(temp['temp']) +' degree Celsius and Humidity is '+ str(hum)+ '%'


def send(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params = {'authorization':'yFJi8aOe0UHAgkjmZoGSKEQbYnu5XhMzBlLr2W6V9cPsfpdRD7HudRiyP5sBhoVQNKJvI6OpwWb2TtmS',
         'sender_id':'FSTSMS',
         'message':message,
         'route':'p',
         'numbers':number,
         'language':'english'
    }
    response=requests.get(url,params=params)
    dic=response.json()

send(num,t)
