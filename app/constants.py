from typing import List, Set
from app.utility.nltk import black_listed_stock_names, get_stock_symbols

SUB_REDDIT = "wallstreetbets"
BLACK_LISTED_STOCK_NAMES: List[str] = black_listed_stock_names()
STOCK_SYMBOLS: Set = get_stock_symbols()