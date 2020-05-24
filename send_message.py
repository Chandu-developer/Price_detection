# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:44:51 2020

@author: 91779
"""

from sinchsms import SinchSMS
#Sending a normal text message to the user
def send_message():
    number = "your_mobile_number_here"
    app_key = "api key"
    app_secrect =   "app secerct key"
    message = 'Hello User, the price of the product is decreased'
    message1  = "Give the link here"
  
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' '%s' to %s" % (message,message1,number)) 
  
    response = client.send_message(number, message,message1) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    # keep trying unless the status retured is Successful 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status'])
