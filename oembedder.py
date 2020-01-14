# python 3.6
# tool to handle making GET requests to Twitter API
# for oembed compatible data
import requests


def get_oembed(tweet):
	"""
	convert a tweepy Status object into a oembeddable tweet
	using Twitter API
	:param tweet: a Tweet object
	:return: json data for that representation of the tweet
	"""

	# api access point
	endpoint = "https://publish.twitter.com/oembed"

	# build tweet url
	screen_name = tweet.json['user']['screen_name']
	id_str = tweet.json['id_str']
	url = f"http://twitter.com/{screen_name}/status/{id_str}"

	params = {
		'url': url,
		'omit_script': True
	}

	r = requests.get(url=endpoint, params=params)
	return r.json()
