#!/usr/bin/python3
'''A function that queries Reddit API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''
    A function that queries Reddit API and returns the number of subscribers
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
    }

    '''Make the API request'''
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    response = requests.get(url, headers=api_headers, allow_redirects=False)

    '''Check if the request was successful (status code 200)'''
    if response.status_code == 200:
        '''Parse the JSON response and extract the number of subscribers'''
        subscribers = response.json().get('data', {}).get('subscribers', 0)
        return subscribers

    '''If the subreddit is invalid or the request fails, return 0'''
    return 0
