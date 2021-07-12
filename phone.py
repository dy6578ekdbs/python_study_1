# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACcaa7398522a143e4b2c586f5fc4924da']
auth_token = os.environ['bce44db41015d9f0c50e22de1e8b56ad']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="뭐해 다윤아? ",
                     from_='+14435683599',
                     to='+821030086578'
                 )