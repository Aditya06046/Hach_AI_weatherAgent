from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low
import requests

class Message(Model):
    text: str

weather_agent = Agent(name="alice", seed="weather_agent")


fund_agent_if_low(weather_agent.wallet.address())

city_name = input("enter city name:")
min_temp = int(input("enter min temperature:"))
max_temp=int(input("enter max tempertature"))
API_KEY = "859ac6047133441da6f54428230510"
API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"

def get_weather():
    try:
        response = requests.get(API_URL)
        print(response)
        weather_json = response.json()
        if response.status_code==200:
            weather = weather_json['current']
            weather = weather['temp_c']
            return weather
        else:
            print("failed to fetch:",response.status_code)
            return 0
    except Exception as e:
        print("error in fetching")
        return None
def monitor_temp_rate():
    mail = []
    temp_today = get_weather()
    if temp_today>max_temp:
        mail.append("Temperature is above",max_temp)
    elif temp_today<min_temp:
        mail.append("Temperature is below",min_temp)
monitor_temp_rate()

if __name__ == "__main__":
    weather_agent.run()
