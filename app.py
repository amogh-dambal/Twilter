from flask import Flask, render_template, request

from filter import authenticate
from tweet import Tweet

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/parse', methods=['GET', 'POST'])
def parse():
	user = request.form['user']
	count = request.form['count']

	api = authenticate()

	if api is not None:
		fetched_tweets = [Tweet(t) for t in api.user_timeline(id=user, count=count)]
		fetched_tweets.sort(key=lambda t: t.likes, reverse=True)
		fetched_tweets = [tweet for tweet in fetched_tweets if not tweet.is_retweet]
	else:
		fetched_tweets = None

	if fetched_tweets is None:
		return render_template('error.html')
	else:
		return render_template('tweets.html', tweets=fetched_tweets)


if __name__ == '__main__':
	app.run(debug=True)
