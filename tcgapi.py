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


class TCGPlayer:
    def __init__(self, token, version):
        header = {"Authorization": f"bearer {token}"}
        self.header = header
        self.version = version

    def ListAllCategories(self, limit=10):
        url = f"http://api.tcgplayer.com/{self.version}/catalog/categories?limit={limit}"

        r = requests.get(url, headers=self.header)

        print(r.text)
    


if __name__ == '__main__':
    tempToken = "ElDRqj0zWLqNXkMyg3FGA0DxGfSS-Vg5kmWWvBrNQkcwBTmZLm7_4NmZnFm17_11EhOUe6PDm8NX0pJJM42uzlwjVFDg5jezoU_tF6huXe0LCscNuCmiqoZES2Me501gzrEipZ7D5CbiT3yVoAjpLNyieJOnG_po8oIJ-kVwsLyAtMNZlcU1pN8wkySB-ux6zndwYnYT-OzLxe1c10VnBTZAyv0pEUZ8vkEn56Xz06ObhFjWQrpqt8_xFJtoOa8Yos_JmpP_P_O9azJ60vW7Eo61hnZqiD0USXpVoqdTMA-tLWAztNar6rTvDCMeYVkZ_6irvg"
    TCG = TCGPlayer(tempToken, "v1.37.0") 

    TCG.ListAllCategories(100)



    # ! Next up: https://docs.tcgplayer.com/reference#catalog_getcategorygroups-1

    