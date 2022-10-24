import requests
import json
import datetime
import pandas
import tweepy
import time

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
X_API_KEY = ""
url = "https://api.newscatcherapi.com/v2/search"
headers = {
    'x-api-key' : X_API_KEY
}
params = {
    'q': 'Climate Change',
    'lang': 'en',
    'to_rank': 10000,
    'page_size': 100,
    'page': 1,
    'from' : yesterday,
    'to' : today,
}
response = requests.get(url, headers=headers, params=params)
results = json.loads(response.text.encode())
print(results)
dataframe = pandas.DataFrame(results['articles'])

keyFile = open('KEYS.txt','r').read().splitlines()
apiKey = keyFile[0]
apiKeySecret = keyFile[1]
accessToken = keyFile[2]
accessTokenSecret = keyFile[3]
bearerToken = keyFile[4]
authenticator = tweepy.OAuthHandler(apiKey, apiKeySecret)
authenticator.set_access_token(accessToken, accessTokenSecret)
print("authenticating")
api = tweepy.API(authenticator, wait_on_rate_limit = True)
print("logged in")

if response.status_code == 200:
    prev = ""
    counter = 0
    for i in dataframe.get('title'):
        if prev == "" or prev != i:
            prev = i
            if len(i) > 256:
                tweet = i[0:252] + "... " + dataframe.get('link')[counter]
                api.update_status(tweet)
            else:
                tweet = i + " " + dataframe.get('link')[counter]
                api.update_status(tweet)
            counter = counter + 1
            time.sleep(600)
        else:
            counter = counter + 1
            continue
else:
    print(results)
    print('ERROR: API call failed.')
