# ISS Viewer 🚀  

A Python script that notifies you via email when the **International Space Station (ISS)** is overhead at your location **and** it’s nighttime, so you can actually see it in the sky.  

## Features  
- Fetches the live ISS position from the [Open Notify API](http://api.open-notify.org/iss-now.json).  
- Checks your location against the ISS position.  
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine whether it’s night.  
- Sends an email alert when both conditions are met.  

## Requirements  
- Python 3.x  
- Internet connection  
- Gmail account (or modify SMTP settings for another email provider)  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Thunderer9506/ISS_Viewer.git
   cd ISS_Viewer
   ```  
2. Install dependencies:  
   ```bash
   pip install requests
   ```  

## Usage  
1. Open the Python file and set your **latitude**, **longitude**, **email address**, and **password**:  
   ```python
   MY_LAT = your_latitude
   MY_LONG = your_longitude
   myemail = "youremail@example.com"
   password = "your_email_password"
   ```  
2. Run the script:  
   ```bash
   python iss_viewer.py
   ```  
3. The script checks every 60 seconds and sends an email if the ISS is overhead at night.  

## Notes  
- You might need to allow "Less secure app access" in your email provider settings for SMTP to work (or create an app password for Gmail).  
- Latitude and longitude should be in decimal degrees.  
- Replace email credentials with environment variables for better security.  

## License  
This project is licensed under the MIT License.  
