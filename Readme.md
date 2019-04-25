Twitter Word Counter
----------
App based on Twitter's API that counts how many times a word is tweeted by an account on its last tweets.

Some considerations to have in mind:
---------
The app does not tweet, like nor retweet any content
The app does not consider retweets nor replies in the count of the words.
The app does not consider links as words
The app considers hashtags as words
The app does not consider stopwords
twitter_word_counter has one source file and two test files:
twitter_api.py

word_count() : Conects to twitter api using consumer_key, consumer_secret, access_token_key, access_token_secret. In order to get them, you need to have a twitter developer account. (To find how to get yours verified go to https://developer.twitter.com/). Then gets among the last 200 tweets, retweets and replies, the latest 50 tweets (does not consider the retweets or the replies)

word_counter(): Counts how many times a word appears on a given array. It does not considerate stopwords.

To execute webpage:
------------
 cd filepath
 
 manage.py runserver port(8000)
 
To execute tests:
--------
 cd filepath
 
 tests.py
 
 dots represent passed tests
 
 E represent error tests