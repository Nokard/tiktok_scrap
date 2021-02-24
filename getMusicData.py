# Importing the settings
from conf import api


def getMusic(musicId):
        
        #Get music Information
        try:
                music = api.getMusicObject(musicId)
        except Exception as e:
                print (e)

        musicAuthor     = music['authorName']
        musicName       = music['title']
        musicPlayUrl    = music['playUrl']
        musicCover      = music['coverLarge'] 
        
        return(musicAuthor, musicName, musicPlayUrl, musicCover)


#musicId = 6703427142346083074
#a = getMusic(musicId)

#print (a[0])

