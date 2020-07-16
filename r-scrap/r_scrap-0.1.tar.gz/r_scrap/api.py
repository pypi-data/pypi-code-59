import logging as log
import os
import json
import requests
import shutil

log.basicConfig(
	filename='r_scrap.log',
	filemode='w', level=log.DEBUG,
	format='%(asctime)s | %(levelname)s: %(message)s')

def fetch_subreddits(limit=None, export=False, user_agent='subreddit.fetch.bot'):
	after = None
	save_directory = 'subreddits'
	fetched_subreddits = 0
	subreddit_index = []
	subreddits = []

	if export:
		try:
			if os.listdir(save_directory):
				log.warn(f'Found {len(os.listdir(save_directory))} {"file" if len(os.listdir(save_directory)) == 1 else "files"} in directory {save_directory}, removing...')
				for file in os.listdir(save_directory):
					os.remove(save_directory + '/' + file)
		except:
			log.warn(f'Directory {save_directory} doesn`t exist, creating...')
			os.mkdir(save_directory)

	while after or not fetched_subreddits: 
		if after:
			req_url = 'https://www.reddit.com/reddits.json?limit=100&after=' + after
		else:
			req_url = 'https://www.reddit.com/reddits.json?limit=100'

		req = requests.get(req_url, headers={'User-agent': user_agent})

		try:
			after = req.json()['data']['after']

			for s in [r['data'] for r in req.json()['data']['children']]:
				subreddit_index.append({
					'id': s['id'],
					'name': s['name'],
					'title': s['title'],
					'url': s['url']
					})

				subreddits.append(s)
				if export:
					#save subreddit to file
					with open(save_directory + '/' + s['id'] + '.json', 'w') as file:
						json.dump(s, file, indent=4)

					#append index to index file
					with open(save_directory + '/' + 'index.json', 'w') as file:
						json.dump(subreddit_index, file, indent=4)

				fetched_subreddits += 1
				log.info(f'Fetched subreddit {s["id"]} for a total of {fetched_subreddits}...')

				if limit and fetched_subreddits >= limit:
					after = None
					break

		except Exception as e:
			#?
			log.error('Exception occured !')
			log.error(str(e))

	return subreddit_index, subreddits

def fetch_submissions(subreddit, limit=None, export=False, user_agent='submission.fetch.bot'):
	# print([(x, subreddit[x]) for x in subreddit])
	after = None
	save_directory = 'submissions'
	fetched_submissions = 0
	submission_index = []
	submissions = []

	if export:
		if os.path.isdir(save_directory):
			try:
				os.rmtree(save_directory)
			except:
				pass
		else:
			try:
				os.mkdir(save_directory)
			except:
				pass

	while after or not fetched_submissions: 
		if after:
			req_url = 'https://www.reddit.com' + subreddit['url'] + '.json?limit=100&after=' + after
		else:
			req_url = 'https://www.reddit.com' + subreddit['url'] + '.json?limit=100'

		req = requests.get(req_url, headers={'User-agent': user_agent})

		try:
			after = req.json()['data']['after']

			for s in [r['data'] for r in req.json()['data']['children']]:
				submission_index.append({
					'id': s['id'],
					'name': s['name'],
					'title': s['title'],
					'permalink': s['permalink']
					})

				if export:
					try:
						os.mkdir(save_directory + '/' + subreddit['id'])
					except:
						pass

				submissions.append(s)
				if export:
					#save subreddit to file
					with open(save_directory + '/' + subreddit['id'] + '/' + s['id'] + '.json', 'w') as file:
						json.dump(s, file, indent=4)

				fetched_submissions += 1
				log.info(f'Fetched submission #{fetched_submissions} {s["id"]} for subreddit {subreddit["id"]}...')

				if limit and fetched_submissions >= limit:
					after = None
					break

		except Exception as e:
			#?
			log.error('Exception occured !')
			log.error(str(e))

	subreddit_submission_index = {'subreddit_id': subreddit['id'], 'subreddit_title': subreddit['title'], 'submissions': submission_index}

	if export:
		with open(save_directory + '/' + subreddit['id'] + '/index.json', 'w') as file:
			json.dump(subreddit_submission_index, file, indent=4)

	return subreddit_submission_index, submissions


