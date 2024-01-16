#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and return
a list containing the titles
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    '''
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
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
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(
            '{}/r/{}/hot/.json'.format(REDDIT_BASE_URL, subreddit),
            headers=api_headers,
            params=params,
            allow_redirects=False
    )

    '''Check if the request was successful (status code 200)'''
    if response.status_code == 200:
        '''Parse the JSON response and append titles to the hot_list'''
        posts = response.json()['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        '''Check if there are more pages (pagination)'''
        after = response.json()['data']['after']
        if after is not None:
            '''Recursively call the function with the next page'''
            return recurse(subreddit, hot_list, after)
        else:
            '''Return the final hot_list'''
            return hot_list

    '''If the subreddit is invalid or the request fails, return None'''
    return None
