#!/usr/bin/python3
"""A function that queries Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Reddit API endpoint for getting subreddit information"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    """Set a custom User-Agent to avoid Too Many Requests error"""
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/58.0.3029.110 Safari/537.3')
    }

    """Make the GET request"""
    response = requests.get(url, headers=headers)

    """Check if the response is successful (status code 200)"""
    if response.status_code == 200:
        """Parse the JSON response"""
        data = response.json()

        """Extract the number of subscribers"""
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        """Return 0 for invalid subreddits or other errors"""
        return 0


if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
