#!/usr/bin/python3
'''A function that queries Reddit API and returns the number of subscribers'''
import requests


REDDIT_BASE_URL = 'https://www.reddit.com'
'''REDDIT api url'''


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers'''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36'
        ])
    }
    '''Make the API request'''
    response = requests.get(
        '{}/r/{}/about/.json'.format(REDDIT_BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        subscribers = response.json()['data']['subscribers']
        return subscribers
    return 0
