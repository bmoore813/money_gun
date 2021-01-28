from enum import Enum
import os
import pathlib

from dotenv import load_dotenv

local_env = os.path.join(os.path.dirname(__file__), "../local.env")
load_dotenv(local_env)

STOCKS_DIRECTORY = os.path.join(pathlib.Path(__file__).parent.absolute(), "stocks")


class StocksFolder(Enum):
    amex_path = os.path.join(STOCKS_DIRECTORY, "amex.csv")
    nasdaq_path = os.path.join(STOCKS_DIRECTORY, "nasdaq.csv")
    nyse_path = os.path.join(STOCKS_DIRECTORY, "nyse.csv")
    master_path = os.path.join(STOCKS_DIRECTORY, "master.csv")


class EnvironmentVariables(Enum):
    """"""

    reddit_app_secret = os.getenv("REDDIT_APP_SECRET")
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_user_name = os.getenv("REDDIT_USER_NAME")
    reddit_login_password = os.getenv("REDDIT_LOGIN_PASSWORD")
    reddit_app_name = os.getenv("REDDIT_APP_NAME")
