import json
import requests
from requests_oauthlib import OAuth1

TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""
TWEET_ID=""

# Generate user context auth (OAuth1)
user_context_auth = OAuth1(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# Totals API endpoint (same for all accounts)
endpoint = f"https://api.twitter.com/2/tweets/{TWEET_ID}?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys"
print(f"endpoint: {endpoint}")

headers = {"Accept-Encoding": "gzip"}
print(f"headers:{headers}")

response = requests.get(endpoint, auth=user_context_auth, headers=headers)

parsed = json.loads(response.text)
pretty_print = json.dumps(parsed, indent=4, sort_keys=True)

print(pretty_print)
