#!/usr/bin/python3
"""A function that queries Reddit API and returns the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Reddit API endpoint for getting subreddit information"""
    url = 'https://www.reddit.com'
    """Reddit's base API URL"""

    """Set a custom User-Agent to avoid Too Many Requests error"""
    headers = {
            'Accept': 'application/json '
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/58.0.3029.110 Safari/537.3'
    }

    """Make the GET request"""
    response = requests.get(url, headers=headers)
    allow_redirects=False

    """Check if the response is successful (status code 200)"""
    if response.status_code == 200:
        """Parse the JSON response"""
        data = response.json()

        """Extract the number of subscribers"""
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
