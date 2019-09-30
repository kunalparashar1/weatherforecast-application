import tkinter as tk
from tkinter import font
import requests


hi = 500
wi = 600

#2c483bb058937a3ff2910c1895f1357e

#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test_function(entry):
    print("this is entry: ", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'problem retrieving the information'

    return final_str
  

def get_weather(city):
    weather_key = '2c483bb058937a3ff2910c1895f1357e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=hi, width=wi )
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
backgorund_label = tk.Label(root, image=background_image)
backgorund_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#4295f5', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('courier', 14))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button( frame, text="Get weather", font=('courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#4295f5', bd=5 )
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('courier', 17), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()