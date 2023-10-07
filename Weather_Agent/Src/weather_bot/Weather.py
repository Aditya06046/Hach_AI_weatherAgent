from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests  #for requesting API's
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
#creating agent
agent = Agent(name="weather", seed="weather_agent")

class Message(Model):
    mail:str


city_name = input("Enter city name:")
min_temp = int(input("Enter min temperature:"))
max_temp=int(input("Enter max tempertature:"))
user_email=input("Enter email to update you when the temperatrue changes:")
time_interval = int(input("Enter time intervel to receive updates in minutes:"))
API_KEY = "859ac6047133441da6f54428230510" # weather API key
API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}" # weather API

# get_weather() is a method to get weather from API
def get_weather():
    try:
        response = requests.get(API_URL)
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

# monitor_temp_rate() is a method used to monitor the present temperature with min and max temperatures user provided
def monitor_temp_rate():
    mail = []
    temp_today = get_weather()  # calling get_weather for taking live temperature from API
    print(temp_today)
    if temp_today>max_temp:
        mail.append(f"Temperature is above {max_temp}")
    elif temp_today<min_temp:
        mail.append(f"Temperature is below {min_temp}")
    else:
        mail.append(f"Temperature is in between {min_temp}-{max_temp}")
    return mail
    
# sent_main() is a method used to send mail to target user if there is change in temperature
async def send_mail(ctx:Context,mail):
    mail_message = MIMEMultipart()  #message object
    mail_message["Subject"] = "Weather update from weather Bot"
    sender_email = os.environ['GMAIL_USER']
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,os.environ['GMAIL_PASSWORD'])
    mail_message.attach(MIMEText(mail[0],'plain'))
    mail_message.attach(MIMEText("\nYou will receive weather updates hourly.",'plain'))
    server.sendmail(sender_email,user_email, mail_message.as_string())  #sending email to target user
    msg_obj = Message(mail=mail[0])
    server.quit()
    await ctx.send(agent.address,msg_obj)
    

# agent will run in a time interval user specified
@agent.on_interval(period=60)
async def weather_monitor(ctx: Context):
    mail = monitor_temp_rate()
    ctx.logger.info(mail)
    if mail:
        await send_mail(ctx,mail)
    


if __name__ == "__main__":
    agent.run()