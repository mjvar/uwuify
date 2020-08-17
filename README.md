# uwuify

A Twitter bot that uwu-ifies tweets. Reply to any tweet with [@uwuify](https://twitter.com/uwuify) and the bot will respond! (Deployed on Heroku with Heroku Scheduler.)

## Requirements
* Python 3.x
* Tweepy

## Developer Usage Tips
The following tips are for anyone looking to adapt this code for their own Twitter bot.

1. Make sure to create an auth.txt file containing the required keys for Twitter API access. For more info about creating a Twitter Developer account, I recommend watching [CS Dojo's excellent video](https://www.youtube.com/watch?v=W0wWwglE1Vc).
2. For deployment to Heroku, make sure to configure requirements.txt to reflect any additional libraries you may use. This allows the Heroku instance to install dependencies.
3. To keep your Twitter bot running constantly, use the [Heroku Scheduler addon](https://devcenter.heroku.com/articles/scheduler). On free versions of Heroku, applications will regularly shut down. Using Scheduler to restart the script at 10-minute intervals will mostly allow for continuous use.