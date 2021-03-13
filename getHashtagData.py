# Importing the settings
from conf import api

results = 10

trending = api.trending(results)

for tik in trending:
    print(tik["desc"])



