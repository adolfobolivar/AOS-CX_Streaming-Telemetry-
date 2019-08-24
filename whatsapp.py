#Enter your account_sid and auth_token from Twilio
#Enter your cellphone number
#Code from https://www.youtube.com/watch?v=98OewpG8-yw "How to Send a WhatsApp Message with Python"


from twilio.rest import Client
import json
from datetime import datetime 

account_sid = 'AAAAAAABBBBBBBBCCCCCCCCCCCCDDDDDD' 
auth_token = 'XXXXXXXXXXYYYYYYYYYYYYZZZZZZZZZZZZZ' 

def alert_message(alert):
    alert = json.loads(alert)
    if alert['type'] == 'notification':
        action = alert['data'][0]['resources'][0]['operation']
        date = datetime.fromtimestamp(alert['data'][0]['resources'][0]['values']['last_configuration_time']).strftime("%d-%m-%Y %I:%M:%S")
        client = Client(account_sid, auth_token) 
        message = client.messages.create( 
                              from_='whatsapp:+14155238886', 
                              media_url='https://aurisscientia.files.wordpress.com/2018/12/15c837d59d26d32a9289d81deefdbfcd.jpg', 
                              body='Config Operation: ' + action + ', done at ' + date,     
                              to='whatsapp:+571234567890' 
                          ) 
        print(message.sid)
