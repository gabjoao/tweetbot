import tweepy
   
auth = tweepy.OAuth1UserHandler(
      'TWITTER_CONSUMER_KEY',
      'TWITTER_CONSUMER_SECRET'
      'TWITTER_ACCESS_TOKEN',
      'TWITTER_ACCESS_TOKEN_SECRET'
    )

api = tweepy.API(auth)

media = api.media_upload(filename="samy.jpg")


try:
   tweet = api.update_status(status="", media_ids= 
   [media.media_id_string])
   print("Tweet enviado")
   
except:
   print("Erro")
