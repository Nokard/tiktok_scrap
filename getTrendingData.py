from TikTokApi import TikTokApi

verifyFp = "verify_klbau46r_u79j4ycy_0IiH_4ChI_9Oyw_bUiUzP864LyR"
api = TikTokApi.get_instance(custom_verufyFp=verifyFp, use_test_endpoint=True)


numVideos = 1
trendingVideos = api.trending(count=numVideos)


for video in trendingVideos:

    videoId = video['id']
    nickName = video['author']['nickname']
    
    print('Video ID {0} | Autor {1}'.format(videoId, nickName))
        



