from flask import Flask, render_template, request

from filter import authenticate, to_json, is_retweet

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
		fetched_tweets = api.user_timeline(id=user, count=count)
		fetched_tweets.sort(key=lambda t: to_json(t)['favorite_count'], reverse=True)
		fetched_tweets = [t for t in fetched_tweets if not is_retweet(t)]
	else:
		fetched_tweets = []

	return render_template('tweets.html', tweets=fetched_tweets)


if __name__ == '__main__':
	app.run(debug=True)
