import pandas as pd
import time
import re
from textblob import TextBlob

from scrapers.bitcoin_scraper import (
    generate_data,
    ml_ify
)
from scrapers.reddit_scraper import (
    scrape_reddit,
    comment_text 
)

def sentiment_analysis(start="2022-07-01", end="2022-07-5"):

    df = generate_data(start, end)
    df = ml_ify(df)

    comments = []
    for unix in df["unix_time"]:
        data = scrape_reddit("submission", "bitcoin", "cryptocurrency", str(int(unix)), str(int(unix-86400)), "30")
        comment_list = str(comment_text(data))
        comments.append(comment_list)
        time.sleep(1)

    df["reddit_comments"] = comments


    def clean_text(text):
        text = re.sub('RT', '', text)
        text = re.sub('#[A-Za-z0-9]+', '', text)
        text = re.sub('\\n', '', text)
        text = re.sub('https?:\/\/\S+', '', text)
        text = re.sub('@[\s]*', '', text)
        text = re.sub('^[\s]+|[\s]+$', '', text)
        return text

    def get_polarity(text):
        return TextBlob(text).sentiment.polarity

    df['cleaned_comments'] = df['reddit_comments'].apply(clean_text)
    df['polarity'] = df['cleaned_comments'].apply(get_polarity)

    df_sentiment = df[['polarity','binary_change']]


    return df_sentiment

# print(sentiment_analysis("2022-07-05", "2022-07-20"))