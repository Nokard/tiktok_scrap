from TikTokApi import TikTokApi
from datetime import datetime
import pandas as pd
import csv
from time import sleep

#from conf import api
from Data.saveData import saveDataCsv

verifyFp = "verify_knhmooha_PyoJh6oX_oeu0_4yFq_8PGS_D1bnbbk8f3J4"

api = TikTokApi.get_instance(custom_verufyFp=verifyFp)


def TimesToDate(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


# Creating a DataFrame
dataCsv = pd.DataFrame()

num = 0
numberTiktoks = 1000000

# Reading a csv with tiktokers
with open('tiktokPerfil.csv') as dados:
        
        csv_reader = csv.reader(dados)
        #  readin a next line after header
        next(csv_reader)

        for dado in csv_reader:

                nameTiktoker = dado[0]

                tiktoksByUser = api.byUsername(nameTiktoker, count=numberTiktoks)
                numVideo = 0
                print(tiktoksByUser)
                
                for tiktoks in tiktoksByUser:
                        print('-------------------------------------------------------------------------------')
                        scrapTime       = str(datetime.now().date())
                        # Author
                        nickname      = tiktoks['author']['nickname']
                        avatarAuthor    = tiktoks['author']['avatarMedium'].join('?x-expires=1618502400&x-signature=xBYgvn8CwzYUwFdpHkAAfqRlzAk%3D')
                        AuthorId        = tiktoks['author']['id']
                        Author          = tiktoks['author']['uniqueId'] 
                        videoId         = tiktoks['video']['id']
                        DurationVideo   = tiktoks['video']['duration']
                        createTime      = str(TimesToDate(tiktoks['createTime']))
                        description     = tiktoks['desc']
                        
                        #Author Status
                        followingCount  = tiktoks['authorStats']['followingCount']      # Pessoas que o perfil segue
                        followerCount   = tiktoks['authorStats']['followerCount']       # total de seguidores do perfil
                        heartCount      = tiktoks['authorStats']['heartCount']          # total de curtidas do perfil 
                        

                        # Stats
                        likesCount      = tiktoks['stats']['diggCount']   
                        commentCount    = tiktoks['stats']['commentCount']
                        shareCount      = tiktoks['stats']['shareCount']
                        playCount       = tiktoks['stats']['playCount']
                        
                        # Music
                        musicId         = tiktoks['music']['id']
                        musicTitle      = tiktoks['music']['title']
                        musicPlayUrl    = tiktoks['music']['playUrl']
                        musicAuthorName = tiktoks['music']['authorName']
                        
                        # Insights = api.get_insights(videoId)
                        
                        # Creating link vídeo
                        VideoLink = 'https://www.tiktok.com/@{0}/video/{1}'.format(Author, videoId)

                        # dadosToCsv = pd.concat([createTime,AuthorId,Author,videoId,description,DurationVideo])
                        data = [numVideo, scrapTime, createTime, avatarAuthor, nickname, Author, description,
                                DurationVideo, VideoLink, likesCount,commentCount, shareCount, playCount,
                                musicId, musicTitle, musicPlayUrl, musicAuthorName]
                        #Chamando a funcção que salva os dados no CSV

                        saveDataCsv(data)
                        numVideo += 1                      
                        #SAlVANDO DADOS NO CSV

                
                print(nameTiktoker, 'Total of Videos: ', numVideo)
             
    