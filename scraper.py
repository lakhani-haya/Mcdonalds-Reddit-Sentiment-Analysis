import praw
import pandas as pd


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="McDonaldsSentimentApp"
)



data = []

for submission in reddit.subreddit("fastfood").hot(limit=100):
    if "mcdonald" in submission.title.lower():
        data.append({
            "title": submission.title,
            "score": submission.score,
            "url": submission.url,
            "created": submission.created_utc
        })

df = pd.DataFrame(data)
df.to_csv("mcdonalds_posts.csv", index=False)
print("Saved to mcdonalds_posts.csv")