import tweepy

api = tweepy.Client(
   consumer_key='7g0R7swnkEPvjGXwF63IWUki5',
   consumer_secret='b0kBZrfC0v9LM0kdqzQyaoYsgZkPNgYwualLzNnuCNOtqpAyhR',
   access_token="1573124468486148096-XzHdi8hH3g9SUp3icACxzu8u0YTJA6",
   access_token_secret='uwmtKZDaa9RJkpAnlMQtZfZmTN1NzsZFmZEqkolsr0TqW'
)

#Código

try:
   tweet = api.create_tweet(text="teste 2")
   print("Tweet enviado")
except:
   print("Erro")