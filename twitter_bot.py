import tweepy
import time

auth = tweepy.OAuthHandler('dxyYICoHxmSG19QnVZCz0VVct','1ojqf9eLGfAZsz4wFiWuyYw7h1Kr55dZyP4a6tXTEIsTB8UK4i')
auth.set_access_token('1400406292645122055-0ThMKUxF1dYRt8fmfpAgZhwUdTwnWn','3dvT8dIPicUe0H5XPz4oYMqzR5ctua48cAkjvUesskNB9')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

string = 'python'
number = 5

for tweet in tweepy.Cursor(api.search, string).items(number):
    try:
        tweet.favorite()
        print('like')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)