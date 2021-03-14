import pandas as pd


def saveDataCsv(*data, **kwargs):
    
    #Using for to read a tuple to transform in list
    for data in data:
        dataCsv = data.append(data, ignore_index=False)

    
    #DataFrame columns
    dataCsv.columns = ['num', 'scrapTime', 'createTime', 'AvatarAuthor', 'AuthorName',  'Author', 'description','DurationVideo','VideoLink', 'likesCount','commentCount', 'shareCount', 'playCount','musicId','musicTitle','musicPlayUrl','musicAuthorName']

    dataCsv.to_csv('Data/tiktokData.csv', encoding='utf-8', index=False)
   