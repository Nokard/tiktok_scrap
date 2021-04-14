import csv


columns = ['num', 'scrapTime', 'createTime', 'AvatarAuthor', 'AuthorName',  'Author', 'description','DurationVideo','VideoLink', 'likesCount','commentCount', 'shareCount', 'playCount','musicId','musicTitle','musicPlayUrl','musicAuthorName']

 
def saveDataCsv(*data, **kwargs):
      
      for data in data:
         
         with open('Data/tiktokData.csv','a', newline="",  encoding='utf-8') as file:
         
            writer = csv.writer(file, delimiter=',')
            writer.writerow(data)