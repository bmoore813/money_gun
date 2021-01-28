"""

"""
from typing import List, Set

import nltk
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd

from app.utility.decorators import type_check
from app.enumerations import StocksFolder
from app.constants import BLACK_LISTED_STOCK_NAMES


@type_check(list)
def nltk_download_corpus(corpuses: List[str]) -> None:
    """"""
    for nltk_corpus in corpuses:

        try:
            nltk.data.find(f"tokenizers/{nltk_corpus}")
        except LookupError:
            nltk.download(nltk_corpus)


def get_stock_symbols() -> Set[str]:
    all_stocks: pd.DataFrame = pd.read_csv(StocksFolder.master_path.value, dtype=object)
    return set(all_stocks["Symbol"].to_list())


def black_listed_stock_names() -> List[str]:
    """"""
    black_list: List[str] = []
    nltk_download_corpus(["words"])
    english_words: List[str] = [w.upper() for w in words.words()]
    for i in get_stock_symbols():
        if i in english_words:
            if len(i) != 1:
                black_list.append(i)
            elif i == "A":
                black_list.append(i)

    return black_list


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
