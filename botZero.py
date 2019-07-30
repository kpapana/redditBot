#!/usr/bin/python
import praw
import re

botZero_quotes = "Please visit India. If you want to know more about visitng India please take a look at https://knowindia.gov.in/"


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("bottestingIndia")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("travel", comment.body, re.IGNORECASE):
            botZero_reply = "BotZero loves touring: " + botZero_quotes
            comment.reply(botZero_reply)
            print(botZero_reply)