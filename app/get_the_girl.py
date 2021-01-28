"""

"""
from typing import List, Set, Dict
import datetime as dttm

import pandas as pd
import praw
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk

from app.enumerations import EnvironmentVariables, StocksFolder
from app.utility.decorators import type_check


@type_check(list)
def nltk_dowload_corpus(corpuses: List[str]) -> None:
    """"""
    for nltk_corpus in corpuses:

        try:
            nltk.data.find(f"tokenizers/{nltk_corpus}")
        except LookupError:
            nltk.download(nltk_corpus)

nltk_dowload_corpus(["stopwords","words"])

all_stocks: pd.DataFrame = pd.read_csv(StocksFolder.master_path.value, dtype=object)
STOCK_SYMBOLS: Set = set(all_stocks["Symbol"].to_list())
from nltk.corpus import words

BLACK_LISTED_STOCK_NAMES = [i for i in STOCK_SYMBOLS if i in words.words()]


del all_stocks


@type_check(float)
def get_date(created_at: float) -> dttm.datetime:
    return dttm.datetime.fromtimestamp(created_at)


@type_check(str)
def toke_it(text: str) -> List[str]:
    return RegexpTokenizer("[\w']+").tokenize(text)


@type_check(list)
def remove_stop_words(tokenized: List[str]) -> List[str]:
    """"""
    stop_words = (
        list(set([i.upper() for i in stopwords.words("english")]))
        + BLACK_LISTED_STOCK_NAMES
    )
    adjusted_corpus: List[str] = [word for word in tokenized if word not in stop_words]
    # print(adjusted_corpus)
    return adjusted_corpus


@type_check(list)
def only_keep_stocks(tokenized: List[str]) -> List[str]:
    """"""

    adjusted_corpus: List[str] = [word for word in tokenized if word in STOCK_SYMBOLS]

    if len(adjusted_corpus) > 0:
        print(f"Before {tokenized}")
        print(adjusted_corpus)

    return adjusted_corpus


def connect_to_reddit() -> praw.Reddit:
    return praw.Reddit(
        client_id=EnvironmentVariables.reddit_client_id.value,
        client_secret=EnvironmentVariables.reddit_app_secret.value,
        user_agent=EnvironmentVariables.reddit_app_name.value,
        username=EnvironmentVariables.reddit_user_name.value,
        password=EnvironmentVariables.reddit_login_password.value,
    )


def get_submission_data(reddit_submission) -> Dict:
    """"""
    return {
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "comms_num": submission.num_comments,
        "created": get_date(float(submission.created)),
        "body": submission.selftext,
    }


if __name__ == "__main__":
    corpus = []
    reddit = connect_to_reddit()
    subreddit = reddit.subreddit("wallstreetbets")
    top_subreddit = subreddit.hot(limit=50_000)
    for submission in top_subreddit:
        submission_data = get_submission_data(submission)
        sub_submission = reddit.submission(submission.id)
        print(submission.selftext)
        child_comments = [comment for comment in submission.comments]
        for com in child_comments:
            try:
                reddit_comment = reddit.comment(com)
                if reddit_comment.body == "":
                    continue
                tokenized_body: List[str] = toke_it(reddit_comment.body.upper())
                tokenized_body: List[str] = remove_stop_words(tokenized_body)
                tokenized_body: List[str] = only_keep_stocks(tokenized_body)
                corpus.append(tokenized_body)

            except Exception as e:
                print(e)
        print("onto new thread")

    # topics_data = pd.DataFrame(topics_dict)
    # topics_data["title"] = topics_data["title"].str.lower()
    # df = topics_data.query('title.str.contains("what are your moves")')

    # print(f"We have {df.shape} threads that need to be processed")

    # for id in df["id"].to_list():
    #     submission = reddit.submission(df["id"].iloc[0])
