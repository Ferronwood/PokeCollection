import pandas as pd
import requests
import pickle
from datetime import datetime


class Auth:
    def __init__(self):
        self.publicKey = "9DA90D6C-1467-4FDD-AA76-AE6EEA9155FF"
        self.privateKey = "6E42ADC9-C683-44AA-B3D8-5B01D0300EB7"
        self.tokenFilename = 'token.p'


    def RequestToken(self):
        body = f"grant_type=client_credentials&client_id={self.publicKey}&client_secret={self.privateKey}"
        r = requests.post('https://api.tcgplayer.com/token', data=body)

        if r.status_code == 200:
            token = r.json()['access_token']
            return token
        
        else:
            print(f"StatusCodeError: f{r.status_code}")


    def SaveToken(self, authToken):
        pickle.dump(authToken, open(self.tokenFilename, "wb"))
        print(f"Token f{self.tokenFilename} saved")


    def LoadToken(self):
        token = pickle.load(open(self.tokenFilename, "rb"))
        return token


    def TestToken(self):
        token = pickle.load(open(self.tokenFilename, "rb"))
        header = {"Authorization": f"bearer {token}"}
        url = "http://api.tcgplayer.com/v1.37.0/catalog/categories?limit=1"

        r = requests.get(url, headers=header)

        if r.status_code == 200:
            return True

        else:
            return False



    


    



        

    