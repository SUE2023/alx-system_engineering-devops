#!/usr/bin/python3
""" Queries the Reddit API recursively and prints a sorted count of given keywords """

import requests

def count_words(subreddit, word_list, after='', word_dict=None):
    ''' A function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    '''
    if word_dict is None:
        word_dict = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_dict:
                word_dict[word_lower] = 0

    if after is None:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count > 0:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'redquery:v1.0.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after', None)
        
        for post in posts:
            title = post['data']['title']
            words = title.split()
            
            for word in words:
                word_lower = word.lower().strip('.,!?-_')
                if word_lower in word_dict:
                    word_dict[word_lower] += 1

    except Exception:
        return None

    return count_words(subreddit, word_list, after, word_dict)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <keywords>".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)

