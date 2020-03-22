from tcgapi import Auth

#  tempToken = "ElDRqj0zWLqNXkMyg3FGA0DxGfSS-Vg5kmWWvBrNQkcwBTmZLm7_4NmZnFm17_11EhOUe6PDm8NX0pJJM42uzlwjVFDg5jezoU_tF6huXe0LCscNuCmiqoZES2Me501gzrEipZ7D5CbiT3yVoAjpLNyieJOnG_po8oIJ-kVwsLyAtMNZlcU1pN8wkySB-ux6zndwYnYT-OzLxe1c10VnBTZAyv0pEUZ8vkEn56Xz06ObhFjWQrpqt8_xFJtoOa8Yos_JmpP_P_O9azJ60vW7Eo61hnZqiD0USXpVoqdTMA-tLWAztNar6rTvDCMeYVkZ_6irvg"
tempToken = "ABC"
#  token = Auth().RequestToken())
token = tempToken

Auth().SaveToken(token)
token = Auth().LoadToken()
test = Auth().TestToken()
print(test)