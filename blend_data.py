import pandas as pd
import time

from scrapers.bitcoin_scraper import (
    generate_data,
    ml_ify
)
from scrapers.reddit_scraper import (
    scrape_reddit,
    comment_text 
)

df = generate_data(start="2022-07-05", end="2022-08-10")
df = ml_ify(df)

comments = []
for unix in df["unix_time"]:
    print(str(int(unix)),str(int(unix-86400)))
    data = scrape_reddit("comment", "bitcoin", "cryptocurrency", str(int(unix)), str(int(unix-86400)), "30")
    comment_list = comment_text(data)
    comments.append(comment_list)
    time.sleep(1)

df["reddit_comments"] = comments

print(df)
