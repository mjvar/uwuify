import tweepy
import emoji
import time

with open("auth.txt", "r") as keys:
	CONSUMER_KEY = keys.readline().strip()
	CONSUMER_SECRET = keys.readline().strip()
	ACCESS_KEY = keys.readline().strip()
	ACCESS_SECRET = keys.readline().strip()

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def uwu(text):
	new = []

	for ch in text:
		if ch == 'r' or ch == 'l':
			new.append('w')
		elif ch == 'R' or ch == 'L':
			new.append('W')
		else:
			new.append(ch)

	if len(new) < 272:
		new.append(" uwu :3 ")
		new.append(emoji.emojize(':pleading_face:', use_aliases=True))

	return ''.join(new)

def already_replied(m):
	mentioner = "@" + m.user.screen_name
	replies = tweepy.Cursor(api.search, q='to:{}'.format(mentioner), since_id=m.id, tweet_mode='extended').items()
	for reply in replies:
		if reply.user.screen_name == "uwuify":
			return True

	return False


def check_for_tweets():
		with open("last_id.txt", "r") as last:
			last_id = last.readline()

		mentions = api.mentions_timeline(last_id)
		if mentions != []:
			print("%s mentions found . . ." % len(mentions))

		try:
			for mention in reversed(mentions):
				last_id = mention.id
				twt = api.get_status(mention.in_reply_to_status_id, include_entities=False)
				my_tweet = "@" + mention.user.screen_name + " " + uwu(twt.text)
				if mention.user.screen_name == "uwuify":
					print("Oops, that's just a tweet fwom uwuify!" + emoji.emojize(':disappointed_relieved:', use_aliases=True))
				elif mention.in_reply_to_screen_name == "uwuify":
					print("Oops, that's just a wepwy to uwuify!" + emoji.emojize(':disappointed_relieved:', use_aliases=True))
				elif mention.text[0:2] == "RT":
					print("Oops, that's a wetweet!" + emoji.emojize(':disappointed_relieved:', use_aliases=True))
				elif already_replied(mention):
					print("Oops, I awweady wepwied to that!" + emoji.emojize(':disappointed_relieved:', use_aliases=True))
				else:
					api.update_status(my_tweet, mention.id, auto_populate_reply_metadata=False)
					print("Wepwied to @" + mention.user.screen_name + ": " + my_tweet)
		except tweepy.TweepError as err:
			print("Something is wwong! " + emoji.emojize(':disappointed_relieved:', use_aliases=True) + str(err))
		except Exception as e:
			print("Big booboo! " + emoji.emojize(':disappointed_relieved:', use_aliases=True) + str(e))
		
		if mentions != []:
			with open("last_id.txt", "w") as last:
				last.write(str(last_id))
	
print("Starting uwuify . . .")
while True:
	check_for_tweets()
	time.sleep(10)