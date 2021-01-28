"""

"""
import pandas as pd
import praw
import datetime as dttm
from enumerations import EnvironmentVariables


def connect_to_reddit() -> praw.Reddit:
    """"""
    # print(EnvironmentVariables.reddit_client_id.value,
    # EnvironmentVariables.reddit_client_id.value,
    # EnvironmentVariables.reddit_app_secret,
    #
    #  EnvironmentVariables.reddit_user_name,
    # EnvironmentVariables.reddit_login_password)

    return praw.Reddit(
        client_id=EnvironmentVariables.reddit_client_id.value,
        client_secret=EnvironmentVariables.reddit_app_secret.value,
        user_agent="money_gun",
        username=EnvironmentVariables.reddit_user_name.value,
        password=EnvironmentVariables.reddit_login_password.value,
    )


topics_dict = {
    "title": [],
    "score": [],
    "id": [],
    "url": [],
    "comms_num": [],
    "created": [],
    "body": [],
}


if __name__ == "__main__":
    reddit = connect_to_reddit()
    # subreddit = reddit.subreddit('wallstreetbets')
    subreddit = reddit.subreddit("Nootropics")
    top_subreddit = subreddit.top(limit=500)
    # print(top_subreddit)
    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
    topics_data = pd.DataFrame(topics_dict)
    print(topics_data)
