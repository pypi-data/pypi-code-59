from urllib.request import Request, urlopen
import json
import random

class SubredditNotFoundError(Exception):
	"""Subreddit you searched for is not found! Please provide a valid name!"""

class Subreddit:
	def __init__(self, subreddit):
		self.subreddit = subreddit
		self.url = None
		self.title = None
		self.upvotes = None
		self.comments = None
		
	def get_random(self):
		error = SubredditNotFoundError("Subreddit you searched for is not found! Please provide a valid name!")
		meme = ""
		while not meme.startswith("https://i.redd.it"):
			url = f"https://api.reddit.com/r/{self.subreddit}/random"
			qq = Request(url)
			randos = list("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
			agent = random.choices(randos, k=random.randint(1,30))
			agent = "".join(agent)
			qq.add_header("User-agent", agent)
			data = json.loads(urlopen(qq).read().decode("utf-8"))
			if not str(data).startswith("["):
				raise error
			else:
				main = data[0]["data"]["children"][0]["data"]
				self.url = main["url"]
				meme = self.url
				self.title = main["title"]
				self.upvotes = main["ups"]
				self.comments = main["num_comments"]