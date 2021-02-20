#Importing the settings
from conf import api


results = 52
tiktoks = api.trending(count=results)

num = 1
for tiktok in tiktoks:
    print(num,' ', tiktok['author']['uniqueId'])

    num += 1


for tiktoks in tiktoksByUser:
                                                
                        scrapTime           = str(datetime.now().date())
                        #Author
                        AuthorName          = tiktoks['author']['nickname']
                        avatarAuthor        = tiktoks['author']['avatarMedium'] 
                        AuthorId            = tiktoks['author']['id']
                        Author              = tiktoks['author']['uniqueId']
                        videoId             = tiktoks['video']['id']
                        DurationVideo       = tiktoks['video']['duration']
                        createTime          = str(TimesToDate(tiktoks['createTime']))
                        description         = tiktoks['desc']
                        
                        #Stats
                        likesCount          = tiktoks['stats']['diggCount']
                        commentCount        = tiktoks['stats']['commentCount']
                        shareCount          = tiktoks['stats']['shareCount']
                        playCount           = tiktoks['stats']['playCount']
                        #Music
                        musicId             = tiktoks['music']['id']
                        musicTitle          = tiktoks['music']['title']

                        try:
                                musicAuthorName     = tiktoks['music']['authorName']
                        except KeyError as Error:
                                print(Error)

                        #Insights = api.get_insights(videoId)

                        #Creating link vídeo
                        VideoLink = 'https://www.tiktok.com/@{0}/video/{1}'.format(Author, videoId)
                        
                        #dadosToCsv = pd.concat([createTime,AuthorId,Author,videoId,description,DurationVideo])

                        data = [[num,scrapTime,createTime,avatarAuthor,AuthorName,Author,description,
                                        DurationVideo,VideoLink,likesCount,
                                        commentCount,shareCount,playCount,
                                        musicId,musicTitle, musicAuthorName]]
                        
                        dataCsv = dataCsv.append(data, ignore_index=False)
                        
                        #print(data)

                        numVideo += 1