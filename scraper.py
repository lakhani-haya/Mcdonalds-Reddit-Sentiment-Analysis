import praw


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="McDonaldsSentimentApp"
)

for submission in reddit.subreddit("fastfood").hot(limit=5):
    print(submission.title)
