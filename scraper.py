import praw


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="McDonaldsSentimentApp"
)

# Filtering only Mcdonald's posts 
for submission in reddit.subreddit("fastfood").hot(limit=50):
    if "mcdonald" in submission.title.lower():
        print(submission.title)
