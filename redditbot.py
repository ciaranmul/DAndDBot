import praw
import os
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("freefolk")

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

else:
    with open("comments_replied_to.txt") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if comment.id not in comments_replied_to:
            if re.search("d&d", comment.body, re.IGNORECASE):
                print("Bot replying to : ", comment.id)
                print("We kinda forgot")

                comments_replied_to.append(comment.id)

with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")
