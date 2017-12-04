"""Script that tweets
:author: Victor Nieves Sanchez
:version: 1.0"""

import tweepy

def login(consumerKey, consumerSecret, accessToken, accessTokenSecret):
    """Login to twitter."""

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)
    ret = {}
    ret['api']= api
    ret['auth'] = auth
    return api

def main():
    """Main function"""

    consumerKey = '' #Your consumer key
    consumerSecret = '' #Your consumer secret
    accessToken = '' #Your access token
    accessTokenSecret = '' #Your access token secret

    msg = "Hello!\nThe script is working!"

    try :
        api = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
        status = api.update_status(status=msg)
        print ("///// YOUR TWEET HAS BEEN SENT ////")
    except tweepy.error.TweepError:
        print ("///// SOMETHING WENT WRONG /////\nMake sure you have written the keys correctly. ")

if __name__ == "__main__":
    main()