import tkinter as tk
import requests #is a third-party library used to make HTTP requests (to fetch weather data from an API)

# Replace with your actual OpenWeatherMap API key
API_KEY = "YOUR_API_KEY_HERE"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text=f"City not found.")
            return

        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        desc = data['weather'][0]['description']
        country = data['sys']['country']

        result = f"📍 {city.title()}, {country}\n🌡️ Temp: {temp}°C\n☁️ Weather: {weather}\n📝 {desc.title()}"
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text="Error fetching data")

# --- GUI Layout ---
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)
city_entry.bind("<Return>", lambda event: get_weather())

search_btn = tk.Button(root, text="Check Weather", font=("Arial", 12), command=get_weather)
search_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

root.mainloop()
