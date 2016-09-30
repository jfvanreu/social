# Sends a search query to the Twitter API and displays results

import config as cfg
import json

def twitterQuery (userQuery, maxCount):
  search_results = cfg.twitter_api.search.tweets(q=userQuery, count=maxCount)
  statuses = search_results['statuses']

  for status in statuses:
    print json.dumps(status['text'], ensure_ascii=False, encoding='utf8', indent=1), status['metadata']['iso_language_code']
  
