import base64
import requests
import datetime
import base64
from urllib.parse import urlencode


client_id = '029fecc3e8c64352b19bbdfb850eb5cd'
client_secret = '7f38c24d9b144f059df3e8dc5906edae'

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"


    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client_secret")

        client_creds = f"{client_id}:{client_secret}"
        client_creds_64 = base64.b64encode(client_creds.encode())
        return client_creds_64.decode()

    def get_token_headers(self):
        client_creds_64 = self.get_client_credentials()
        return {
            "Authorization" : f"Basic {client_creds_64}"
    
        }

    def get_token_data(self):
        return {
            "grant_type" : "client_credentials"   
        }
        
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range (200, 299):
            raise Exception("Could not authenticate client")
        data = r.json()
        now = datetime.datatime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] #seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now #returns a boolean value
        return True

    def get_access_token(self):
        # look for token
        token = self.access_token
        # check if token has expired or not
        expires = self.access_token_expires
        # compares expiration from now
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth
            return self.get_access_token
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token
    
    def search (self, query, search_type='artist'):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": query,"type": search_type}) #q = query 

        lookup_url = f"{endpoint}?{data}"
        r = requests.get(endpoint, data=data, headers=headers)
        if r.status_code in range(200,299):
          return {}
        return r.json()

spotify = SpotifyAPI(client_id, client_secret)
spotify.search("Time", search_type = "Track")





        
        

