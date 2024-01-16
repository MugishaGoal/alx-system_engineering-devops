#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }

    '''Make the API request'''
    REDDIT_BASE_URL = 'https://www.reddit.com'
    response = requests.get(
            '{}/r/{}/hot/.json'.format(REDDIT_BASE_URL, subreddit),
            headers=api_headers,
            params={'limit': 10},
            allow_redirects=False
    )

    '''Check if the request was successful (status code 200)'''
    if response.status_code == 200:
        '''Parse the JSON response and print titles of the first 10 posts'''
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        '''If the subreddit is invalid or the request fails, print None'''
        print(None)
