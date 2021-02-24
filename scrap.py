from TikTokApi import TikTokApi
from datetime import datetime
import pandas as pd
import csv
from time import sleep

from tqdm import tqdm
# Importing the settings
from conf import api


from getMusicData import getMusic


def TimesToDate(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


# Creating a DataFrame
dataCsv = pd.DataFrame()

num = 0
numberTiktoks = 1000

# Reading a csv with tiktokers
with open('tiktokPerfil.csv') as dados:
        
        csv_reader = csv.reader(dados)
        #  readin a next line after header
        next(csv_reader)

        for dado in csv_reader:
                nameTiktoker = dado[0]

                tiktoksByUser = api.byUsername(nameTiktoker, count=numberTiktoks)
                numVideo = 1

                for tiktoks in tiktoksByUser:

                        scrapTime = str(datetime.now().date())
                        # Author
                        AuthorName = tiktoks['author']['nickname']
                        avatarAuthor = tiktoks['author']['avatarMedium']
                        AuthorId = tiktoks['author']['id']
                        Author = tiktoks['author']['uniqueId']
                        videoId = tiktoks['video']['id']
                        DurationVideo = tiktoks['video']['duration']
                        createTime = str(TimesToDate(tiktoks['createTime']))
                        description = tiktoks['desc']

                        # Stats
                        likesCount = tiktoks['stats']['diggCount']
                        commentCount = tiktoks['stats']['commentCount']
                        shareCount = tiktoks['stats']['shareCount']
                        playCount = tiktoks['stats']['playCount']
                        # Music
                        musicId = tiktoks['music']['id']
                        musicTitle = tiktoks['music']['title']

                        try:
                                musicAuthorName = tiktoks['music']['authorName']
                        except KeyError as Error:
                                print(Error)


                        
                        # Insights = api.get_insights(videoId)

                        # Creating link vídeo
                        VideoLink = 'https://www.tiktok.com/@{0}/video/{1}'.format(Author, videoId)

                        # dadosToCsv = pd.concat([createTime,AuthorId,Author,videoId,description,DurationVideo])

                        data = [[numVideo, scrapTime, createTime, avatarAuthor, AuthorName, Author, description,
                                DurationVideo, VideoLink, likesCount,commentCount, shareCount, playCount,
                                musicId, musicTitle, musicAuthorName]]

                        dataCsv = dataCsv.append(data, ignore_index=False)

                        # print(data)

                        numVideo += 1

                print(nameTiktoker, 'Total of Videos: ', numVideo)

        dataCsv.columns = ['num', 'scrapTime', 'createTime', 'AvatarAuthor', 'AuthorName', 'Author', 'description',
        'DurationVideo', 'VideoLink', 'likesCount','commentCount', 'shareCount', 'playCount','musicId', 'musicTitle', 'musicAuthorName']

        dataCsv.to_csv('Data/tiktokData.csv', encoding='utf-8', index=False)
