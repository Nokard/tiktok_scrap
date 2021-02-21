# Importing the settings
from conf import api
import datetime

results = 52
tiktoks = api.trending(count=results)

num = 1
for tiktok in tiktoks:
        print(tiktok)