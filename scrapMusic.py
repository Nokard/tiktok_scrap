#Importing the settings
from conf import api

musicId = '6839154166166801157'

tiktoks = api.trending()



for tiktok in tiktoks:
    print(tiktok['music']['id'])