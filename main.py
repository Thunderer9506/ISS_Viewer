import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 1.0000 # Your latitude
MY_LONG = 1.0000 # Your longitude

myemail = "your email address"
password = "your password"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and  MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead == True and is_night == True:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=myemail,password=password)
        connection.sendmail(
            from_addr=myemail,to_addrs=myemail,
            msg="Subject:Go outside\n\n"+"The ISS is above you")