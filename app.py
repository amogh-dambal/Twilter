from flask import Flask, render_template, request

from filter import authenticate
from tweet import Tweet
from oembedder import get_oembed

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/parse', methods=['GET', 'POST'])
def parse():
	user = request.form['user']
	count = request.form['count']

	# setup API to make our request
	api = authenticate()

	if api is not None:
		fetched_tweets = [Tweet(t) for t in api.user_timeline(id=user, count=count)]

		# descending sort by likes and filter tweets to ignore retweets
		fetched_tweets.sort(key=lambda t: t.likes, reverse=True)
		fetched_tweets = [tweet for tweet in fetched_tweets if not tweet.is_retweet]

		embeddable_tweets = [get_oembed(tweet) for tweet in fetched_tweets]
	else:
		embeddable_tweets = None

	if embeddable_tweets is None:
		return render_template('error.html')
	else:
		return render_template('tweets.html', emb=embeddable_tweets)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
