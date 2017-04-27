import newsapi
import requests
import json
import os

from newsapi.articles import Articles
from newsapi.sources import Sources

a = Articles(API_KEY="537b165a4f314fedae8cb39788d4d713")
s = Sources(API_KEY="537b165a4f314fedae8cb39788d4d713")

res = a.get(source="daily-mail")['articles']
bbc = a.get(source="bbc-news")['articles']
telegraph = a.get(source="the-telegraph")['articles']
guardian = a.get(source="the-guardian-uk")['articles']

# results = s.get_by_country("gb").sources
# # s.get_by_category("politics")

#resultsString = ''.join(str(e) for e in results)

filename = 'news_stream.py'

# for 

with open(filename, 'a') as file:
    for result in guardian:
        print(result['title'])
        # If you want other things from the tweet object you can specify it here
        file.write(result['title'] + os.linesep)