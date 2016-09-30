# Connects to Twitter API and detects trending topics
import twitter
import json
from collections import Counter
import matplotlib.pyplot as plt

import credentials as cr

auth=twitter.oauth.OAuth(cr.OAUTH_TOKEN, cr.OAUTH_TOKEN_SECRET,cr.CONSUMER_KEY, cr.CONSUMER_SECRET)

# request access to the Twitter API using credentials
twitter_api = twitter.Twitter(auth=auth)


# request latest statuses
count=100

q='#Hillary'
search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

# extracting text, screen names and hashtags from tweets
status_texts = [status['text'] 
						for status in statuses]
screen_names = [user_mention['screen_name'] 
						for status in statuses
						    for user_mention in status['entities']['user_mentions']]
						    
hashtags = [hashtag['text']
				for status in statuses
					for hashtag in status['entities']['hashtags']]
					
#split tweets text into words
words = [w
		  for t in status_texts
		      for w in t.split()]

for label, data in (('Word', words), ('Screen Name', screen_names), ('Hashtags', hashtags)):
  c = Counter(data)
  plt.hist(c.values())
  
  #Add a title and y-label
  plt.title(label)
  plt.ylabel("Number of items in bin")
  plt.xlabel("Bins (number of times an item appeared")
  
  #...display the figure
  plt.show()
  
  
  




						    