import tweepy
   
auth = tweepy.OAuth1UserHandler(
      '7g0R7swnkEPvjGXwF63IWUki5',
      'b0kBZrfC0v9LM0kdqzQyaoYsgZkPNgYwualLzNnuCNOtqpAyhR',
      '1573124468486148096-XzHdi8hH3g9SUp3icACxzu8u0YTJA6',
      'uwmtKZDaa9RJkpAnlMQtZfZmTN1NzsZFmZEqkolsr0TqW'
    )

api = tweepy.API(auth)

media = api.media_upload(filename="samy.jpg")


try:
   tweet = api.update_status(status="", media_ids= 
   [media.media_id_string])
   print("Tweet enviado")
   
except:
   print("Erro")
