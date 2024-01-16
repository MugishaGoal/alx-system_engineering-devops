#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses
the title of all hot articles
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    '''
    A recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords.
    '''
    if counts is None:
        counts = {}

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
    BASE_URL = 'https://www.reddit.com'
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(
        '{}/r/{}/hot/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        params=params,
        allow_redirects=False
    )

    '''Check if the request was successful (status code 200)'''
    if response.status_code == 200:
        '''Parse the JSON response and update word counts'''
        posts = response.json()['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word] = counts.get(word, 0) + 1

        '''Check if there are more pages (pagination)'''
        after = response.json()['data']['after']
        if after is not None:
            '''Recursively call the function with the next page'''
            return count_words(subreddit, word_list, after, counts)
        else:
            '''Print the sorted results'''
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print('{}: {}'.format(word, count))
            return None

    '''If the subreddit is invalid or the request fails, return None'''
    return None
