"""

"""
from typing import List, Set, Dict
from collections import Counter
import datetime as dttm

from app.utility.decorators import type_check
from app.engines.reddit import connect_to_reddit
from app.constants import SUB_REDDIT
from app.utility.nltk import (
    black_listed_stock_names,
    get_stock_symbols,
    toke_it,
    remove_stop_words,
)

BLACK_LISTED_STOCK_NAMES: List[str] = black_listed_stock_names()
STOCK_SYMBOLS: Set = get_stock_symbols()


@type_check(float)
def get_date(created_at: float) -> dttm.datetime:
    return dttm.datetime.fromtimestamp(created_at)


@type_check(list)
def only_keep_stocks(tokenized: List[str]) -> List[str]:
    """"""

    adjusted_corpus: List[str] = [word for word in tokenized if word in STOCK_SYMBOLS]

    if len(adjusted_corpus) > 0:
        print(f"Before {tokenized}")
        print(adjusted_corpus)

    return adjusted_corpus


def get_submission_data(reddit_submission) -> Dict:
    """"""
    return {
        "title": reddit_submission.title,
        "score": reddit_submission.score,
        "id": reddit_submission.id,
        "url": reddit_submission.url,
        "comms_num": reddit_submission.num_comments,
        "created": get_date(float(reddit_submission.created)),
        "body": reddit_submission.selftext,
    }


def main() -> None:
    corpus = []
    reddit = connect_to_reddit()
    subreddit = reddit.subreddit(SUB_REDDIT)
    top_subreddit = subreddit.hot(limit=50_000)
    for submission in top_subreddit:
        submission_data: Dict = get_submission_data(submission)
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


if __name__ == "__main__":
    main()
