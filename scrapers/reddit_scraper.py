import requests

def scrape_reddit(endpoint = "comment", term = "", subreddit = "", end = None, begin = None, limit="1000"):
    url = "https://api.pushshift.io/reddit/{}/search/?q={}&subreddit={}&before={}&after={}&limit={}"
    new_url = url.format(endpoint, term, subreddit, end, begin, limit)

    print(new_url)
    data = requests.get(new_url)

    return data.json()["data"]

def comment_text(data):
    res = []
    for comment in data:
        res.append(comment["body"])
    return res

# data = scrape_reddit("comment", "bitcoin", "cryptocurrency", "1660458309", "1660370077", "50")

# print(comment_text(data))