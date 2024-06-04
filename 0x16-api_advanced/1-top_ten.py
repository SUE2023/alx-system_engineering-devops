#!/usr/bin/python3
'''
This module contains the function top_ten.
'''
import requests
from sys import argv

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Lizzie'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is OK
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        
        # Check if the required keys exist in the response
        if 'data' not in data or 'children' not in data['data']:
            print(None)
            return
        
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except requests.RequestException as e:
        # Handle any request exceptions
        print(None)
    except ValueError:
        # Handle JSON decoding errors
        print(None)
    except Exception:
        # Handle any other exceptions
        print(None)

if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: {} <subreddit>".format(argv[0]))


