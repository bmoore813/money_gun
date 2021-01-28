import requests
from pprint import pprint

from app.enumerations import EnvironmentVariables


# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
client_auth = requests.auth.HTTPBasicAuth(
    EnvironmentVariables.reddit_client_id.value,
    EnvironmentVariables.reddit_app_secret.value,
)

# here we pass our login method (password), username, and password
data = {
    "grant_type": "password",
    "username": EnvironmentVariables.reddit_user_name.value,
    "password": EnvironmentVariables.reddit_login_password.value,
}

# setup our header info, which gives reddit a brief description of our app
headers = {"User-Agent": "MyBot/0.0.1"}

# send our request for an OAuth token
res = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=client_auth,
    data=data,
    headers=headers,
)

# convert response to JSON and pull access_token value
TOKEN = res.json()["access_token"]

# add authorization to our headers dictionary
headers = {**headers, **{"Authorization": f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests

# res = requests.get("https://oauth.reddit.com/r/wallstreetbets/hot",
#                    headers=headers)
#
# print(res.json())  # let's


# data = requests.get('https://oauth.reddit.com/r/wallstreetbets/comments/l6ea1b/what_are_your_moves_tomorrow_january_28_2021/' ,headers=headers)
#
# print(data.json())


new = requests.get(
    "https://oauth.reddit.com/r/wallstreetbets/comments/l6ea1b/what_are_your_moves_tomorrow_january_28_2021/gl18oyw/",
    headers=headers,
)

print(new.json())
