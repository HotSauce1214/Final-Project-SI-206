
!pip install requests
import requests
import base64
import datetime

client_id = '029fecc3e8c64352b19bbdfb850eb5cd'
client_secret = '7f38c24d9b144f059df3e8dc5906edae'

# do a lookup for our token
# this token is for future requests

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type" : "client_credentials"
}
token_header = {
    "Authorization" : "Basic <base64 encoded client_id:client_secret>"
}

#this gets our token
r = requests.post(token_url, data=token_data, headers=token_header)
valid_request = r.status_code in range (200, 299)

if valid_request:
    token_response_data = r.json()
    now = datetime.datatime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] #seconds
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now #returns a boolean value
