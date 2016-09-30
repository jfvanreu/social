# Connects to Twitter API and identifies most retweeted tweets
import twitter
import json
from collections import Counter
from prettytable import PrettyTable
import credentials as cr

auth=twitter.oauth.OAuth(cr.OAUTH_TOKEN, cr.OAUTH_TOKEN_SECRET,cr.CONSUMER_KEY, cr.CONSUMER_SECRET)

# request access to the Twitter API using credentials
twitter_api = twitter.Twitter(auth=auth)


# request latest statuses
count=100

q='#trump'
search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

# Seeking most popular retweets using a comprehension list

retweets = [
            # Store following information for all retweets
            (status['retweet_count'],
            status['retweeted_status']['user']['screen_name'],
			status['text'])
			 
			 # ...for each status in statuses
			 for status in statuses
			 
			 # ....as long as the status meets this condition
			 if status.has_key('retweeted_status')
			 ]

# Extract the 5 most popular retweets and print in pretty table

pt=PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]
pt.max_width['Text']=50
pt.align='l'
print pt



