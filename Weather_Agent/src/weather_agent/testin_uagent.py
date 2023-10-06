from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low
import requests  #for requesting apis
import smtplib

agent = Agent(name="weather", seed="weather_agent")

class Message(Model):
    mail:str



# @weather_agent.on_event("startup")
# async def introduce_agent(ctx: Context):
#     #ctx.logger.info(f"Hello! I'm a weather agent designed to give you the current weather of any city")
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
    print(temp_today)
    if temp_today>max_temp:
        mail.append(f"Temperature is above {max_temp}")
    elif temp_today<min_temp:
        mail.append(f"Temperature is below {min_temp}")
    else:
        print("No difference in temperature")
    return mail
    

async def send_mail(ctx:Context,mail):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("modugulla.bhargav@gmail.com","zwhv swwf kmtk woyb")
    server.sendmail("modugulla.bhargav@gmail.com","medagam.karthik@gmail.com", mail[0])
    msg_obj = Message(mail=mail[0])
    server.quit()
    await ctx.send(agent.address,msg_obj)
    


@agent.on_interval(period=3600.0)
async def weather_monitor(ctx: Context):
    mail = monitor_temp_rate()
    ctx.logger.info(mail)
    if mail:
        await send_mail(ctx,mail)
    else:
        print("no difference in temp")
    


if __name__ == "__main__":
    agent.run()