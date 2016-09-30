# Trending topics function

import config as cfg
import json

#WORLD_WOE_ID=1 #The entire world
#US_WOE_ID=23424977 #The United States
#MRY_WOE_ID=12797089 #Monterey, CA



def trendingTopics(location):
  """returns trending topics
     with location 0 for world and Yahoo! Geo location ID for others"""
     
  trends=[]
  trends = cfg.twitter_api.trends.place(_id=location)
  for trend in trends[0]['trends']:
    print trend['name'], trend['tweet_volume']
    
