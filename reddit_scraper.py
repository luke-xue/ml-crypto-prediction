import requests

def scrape_reddit(endpoint = "comment", term = "", subreddit = "", begin = None, end = None, limit="1000"):
    url = "https://api.pushshift.io/reddit/{}/search/?q={}&subreddit={}&before={}&after={}&limit={}"
    new_url = url.format(endpoint, term, subreddit, begin, end, limit)

    print(new_url)
    data = requests.get(new_url)

    return data.json()

print(scrape_reddit("comment", "bitcoin", "cryptocurrency", "1660458309", "1660370077", "1000"))