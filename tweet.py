import copy


class Tweet:
	def __init__(self, status_obj):
		self.json = copy.deepcopy(status_obj._json)
		self.text = self.json['text']
		self.likes = self.json['favorite_count']
		self.is_retweet = True if 'retweeted_status' in self.json else False

	def __repr__(self):
		return f"{self.text}\nlikes: {self.likes}"

	def __str__(self):
		return f"{self.text}\nlikes: {self.likes}"
