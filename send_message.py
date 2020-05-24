# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:44:51 2020

@author: 91779
"""

from sinchsms import SinchSMS
#Sending a normal text message to the user
def send_message():
    number = "7799004638"
    app_key = "084f3b8e7a1d431b9bb3a9b0f422f693"
    app_secrect =   "74c4e39891a84db3bb9cf5e640755a05"
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