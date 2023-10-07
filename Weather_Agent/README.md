# Weather Notifier Bot

Weather Notifier Bot is a Python project created using the uAgent library and Poetry virtual environment. It allows users to receive email notifications when the temperature in a user-specified location exceeds certain minimum and maximum thresholds. The project utilizes the WeatherAPI for obtaining real-time temperature data and the 'smtplib' library for sending email notifications.

## Features

- User-friendly command-line interface.
- Customizable temperature thresholds.
- Real-time weather data retrieval using WeatherAPI.
- Email notifications for temperature alerts.

## Requirements

- Python 3.9
- Poetry (for managing dependencies)
- uAgents library
- smtplib
- WeatherAPI API key (Sign up at https://www.weatherapi.com/  to   obtain an API key)
- A Gmail account (for sending email notifications)

## Installation

1. Clone this repository:
git clone https://github.com/Aditya06046/Hack_AI_weatherAgent

2. Install poetry
   Mac:     curl -sSL https://install.python-poetry.org | python3 -
            poetry install
   windows: pip install poetry
   
 ## Usage
 
  Run the Weather Notifier Bot:
 
  cd Hach_AI_weatherAgent\Weather_Agent\src\weather_bot
  Run  python weather.py
  
  1.Follow the prompts to specify the location, minimum temperature threshold, and maximum temperature threshold.
  2.The bot will check the temperature at the specified location using WeatherAPI and send an email notification if the temperature exceeds the specified 
    thresholds.

  ## Contributing
  
  If you'd like to contribute to this project, please fork the repository and submit a pull request.
    
  ## Acknowledgments

 - WeatherAPI for providing real-time weather data.
 - Python for its versatility.
 - uAgent library for creating a user-friendly command-line interface.
 - Poetry for dependency management.
 - smtplib library for sending email notifications.




