# Connects to Twitter API and detects trending topics
import twitter
import json
from collections import Counter
from prettytable import PrettyTable

import config as cfg


def twitterCount(twitterQuery, maxResults):
  search_results = cfg.twitter_api.search.tweets(q=twitterQuery, count=maxResults)
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
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:20] ]
    pt.align[label], pt.align['Count'] = 'l', 'r'   #set the column alignment
    print pt
  
"""#Lexical Diversity

# Create function for lexical diversity
def lexical_diversity(tokens):
  return 1.0*len(set(tokens))/len(tokens)

# Create a function for the average number of words per tweet
def average_words(statuses):
  total_words = sum([len(words.split()) for words in status_texts])
  return 1.0*total_words/len(statuses)
  
print lexical_diversity(words)
print average_words(statuses)"""







						    