#!/usr/bin/python3.10
import tweepy
import datetime

keyFile = open('KEYS.txt','r').read().splitlines()
apiKey = keyFile[0]
apiKeySecret = keyFile[1]
accessToken = keyFile[2]
accessTokenSecret = keyFile[3]
bearerToken = keyFile[4]
weeks = keyFile[5]

authenticator = tweepy.OAuthHandler(apiKey, apiKeySecret)
authenticator.set_access_token(accessToken, accessTokenSecret)
print("authenticating")
api = tweepy.API(authenticator, wait_on_rate_limit = True)
print("logged in")
now = datetime.datetime.now()
day = now.weekday()
if day == 6:
    weeks = str(int(weeks) + 1)
    filename = "boruto.jpg"
    status = "It has been " + weeks + " weeks (" + str(int(weeks)*7) + " days) since the last manga-canon BORUTO episode."
    api.update_status_with_media(filename = filename, status = status)
    with open('KEYS.txt','w') as page:
        page.write(apiKey + "\n")
        page.write(apiKeySecret + "\n")
        page.write(accessToken + "\n")
        page.write(accessTokenSecret + "\n")
        page.write(bearerToken + "\n")
        page.write(weeks + "\n")
    page.close()
    print("posted")
