import json
import tweepy


# set authentication and load tweepy API
def authenticate(credfile='twitter_creds.json'):
	with open(credfile, 'r') as cf:
		creds = json.load(cf)

	try:
		auth = tweepy.OAuthHandler(
			creds['CONSUMER_KEY'],
			creds['CONSUMER_SECRET']
		)

		auth.set_access_token(
			creds['ACCESS_TOKEN'],
			creds['ACCESS_SECRET']
		)

		return tweepy.API(auth)

	except KeyError as ke:
		print("Error: could not authenticate." + str(ke))
		return None



