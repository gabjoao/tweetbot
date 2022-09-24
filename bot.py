import tweepy
import time
   
auth = tweepy.OAuth1UserHandler(
      'TWITTER_CONSUMER_KEY',
      'TWITTER_CONSUMER_SECRET'
      'TWITTER_ACCESS_TOKEN',
      'TWITTER_ACCESS_TOKEN_SECRET'
    )

api = tweepy.API(auth)

def _main_():
   samy1 = api.media_upload(filename="samy2.jpg")
   
   
   #Tweets das fotos
   try:
      tweet = api.update_status(status="", media_ids=[samy1.media_id_string])
      print("Tweet enviado")
   
   except:
      print("Erro")
   


while True:
   _main_()
   time.sleep(86400) #A cada 24h
