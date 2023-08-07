import requests
from dotenv import dotenv_values
env = dotenv_values(".env")

class Auth:
    # Credentials
    def __init__(self, client_id, client_secret, mid, auth_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.mid = mid
        self.auth_uri = auth_uri
        self.access_token = None

    def get_access_token(self):
        '''
        Fetch access code
        '''
        uri = self.auth_uri + 'v2/token'
        body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "account_id": self.mid
        }
        response = requests.post(uri, data=body)
        
        try:

            self.access_token = response.json()['access_token']
            if response.status_code == 200:
                print('Access Code retrieved')
            else:
                print('Access Code retrieval unsuccessful')

        except ValueError:
            print(ValueError)
    
