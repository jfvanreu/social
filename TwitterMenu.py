"""Small application to access Twitter API
   Usage::
     1. Provides trending topics
     2. Search the Twitterverse
     3. Show Popularity graphic 
     4. Quit

"""
# import necessary packages
import twitter
import prettytable
import credentials as cr
import TwitterTrendingTopics as ttt
import TwitterQuery as tq
import TwitterCount as tc
import config as cfg

# build menu as a hash
menu = {}
menu['0']="Welcome to the Twitter Menu"
menu['1']="[1] Display trending topics"
menu['2']="[2] Search the Twitterverse"
menu['3']="[3] Show popularity graphic"
menu['4']="[4] Exit"

# sort the hash
options=menu.keys()
options.sort()
menusize=len(options)-1

# connect to Twitter API
auth=twitter.oauth.OAuth(cr.OAUTH_TOKEN, cr.OAUTH_TOKEN_SECRET, cr.CONSUMER_KEY, cr.CONSUMER_SECRET)

# request access to the Twitter API using credentials
cfg.twitter_api = twitter.Twitter(auth=auth)

while True:
  # display menu
    for entry in options:
      print menu[entry]
 
  # prompt user
    try:
      choice=int(raw_input("Please select a menu option: "))        
      
      # run user selection 
      if choice == 1:
        # call trending topics function
        print 'Trending topics on Twitter:'
        ttt.trendingTopics(1)
      elif choice == 2:
        # request search criteria and call query function
        search_query=(raw_input("Please enter your search criteria: "))
        tq.twitterQuery(search_query, 100)
      elif choice == 3:
        # request search topic to count and call count function
        search_query=(raw_input("Please enter the topic for which you'd like to see a count: "))
        print 'The popularity count associated to this word is'
        tc.twitterCount(search_query, 100)
      elif choice == 4:
        # quit application
        break
      elif choice >= menusize:
        print "Please pick an option between 1 and", (menusize)
    
    except ValueError:
      print "Please enter a number between 1 and", (menusize)

    