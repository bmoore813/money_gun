from enum import Enum
import os

from dotenv import load_dotenv

local_env = os.path.join(os.path.dirname(__file__), "../local.env")
load_dotenv(local_env)

stocks_directory = "/Users/brian-moore/PycharmProjects/money_gun/app/stocks"


class StocksFolder(Enum):
    amex_path = os.path.join(stocks_directory, "amex.csv")
    nasdaq_path = os.path.join(stocks_directory, "nasdaq.csv")
    nyse_path = os.path.join(stocks_directory, "nyse.csv")
    master_path = os.path.join(stocks_directory, "master.csv")


class EnvironmentVariables(Enum):
    """"""

    reddit_app_secret = os.getenv("REDDIT_APP_SECRET")
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_user_name = os.getenv("REDDIT_USER_NAME")
    reddit_login_password = os.getenv("REDDIT_LOGIN_PASSWORD")
