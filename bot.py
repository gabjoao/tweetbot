import tweepy
import time
import random
   
auth = tweepy.OAuth1UserHandler(
      'TWITTER_CONSUMER_KEY',
      'TWITTER_CONSUMER_SECRET'
      'TWITTER_ACCESS_TOKEN',
      'TWITTER_ACCESS_TOKEN_SECRET'
    )

api = tweepy.API(auth)

#Função para os tweets
def tweetar(fotos, a):
   try:
      tweet = api.update_status(status="", media_ids=[fotos[a].media_id_string])
      print("Tweet enviado, foto ", a+1)
      
   except:
      print("Erro ao tweetar.")

#Função main
def _main_():
   
   #Criação dos objetos das fotos
   samy1 = api.media_upload(filename='fotos\samy1.jpg')
   samy2 = api.media_upload(filename="fotos\samy2.jpg")
   samy3 = api.media_upload(filename="fotos\samy3.jpg")
   samy4 = api.media_upload(filename="fotos\samy4.jpg")
   samy5 = api.media_upload(filename="fotos\samy5.jpg")
   samy6 = api.media_upload(filename="fotos\samy6.jpg")
   
   amy1 = api.media_upload(filename="fotos\my1.jpg")
   amy2 = api.media_upload(filename="fotos\my2.jpg")
   amy3 = api.media_upload(filename="fotos\my3.jpg")
   amy4 = api.media_upload(filename="fotos\my4.jpg")
   amy5 = api.media_upload(filename="fotos\my5.jpg")
   amy6 = api.media_upload(filename="fotos\my6.jpg")
   amy7 = api.media_upload(filename="fotos\my7.jpg")
   amy8 = api.media_upload(filename="fotos\my8.jpg")
   amy9 = api.media_upload(filename="fotos\my9.jpg")
   
   #Lista com os objetos
   fotos = [samy1, samy2, samy3, samy4, samy5, samy6, amy1, amy2, amy3, amy4, amy5,
            amy6, amy7, amy8, amy9]
    
   #Tweets das fotos
   a = random.randrange(15)
   tweetar(fotos, a)

#Intervalo para as postagens
while True:
   _main_()
   time.sleep(86400) #24hrs