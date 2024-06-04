#!/usr/bin/python3
'''Recursive function'''
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        
        # Check if the response contains valid JSON
        if response.headers.get('Content-Type') != 'application/json':
            return None
        
        results = response.json().get("data")
        if not results:
            return None

        after = results.get("after")
        count += results.get("dist")

        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError:
        print("Error: Unable to parse JSON")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = recurse(sys.argv[1])
        if result:
            print(result)
        else:
            print(None)
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))

