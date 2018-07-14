import os
import json
from simhash import Simhash
from itertools import product

path = 'news/零知识证明：区块链隐私保护利器'

websites = []
contents = []
articles = []
for filename in os.listdir(path):
    print(filename)
    article = json.load(open(os.path.join(path, filename)))
    content = article['content']
    website = article['website']
    websites.append(website)
    contents.append(content)
    articles.append(article)

ham_mat = [
    [0 for i in titles] for j in titles
]
echarts_container =[]

def distance(c1, c2):
    dist = Simhash(c1).distance(Simhash(c2))
    return dist

for article_1, article_2 in product(articles, articles):
    dist = distance(article_1['content'], article_2['content'])
    row = websites.index(article_1['website'])
    col = websites.index(article_2['website'])
    print(row, col, titles[row], titles[col], dist)
    ham_mat[row][col] = dist
    echarts_container.append([
        row,
        col,
        dist
    ])

print(titles)
print(ham_mat)
print(echarts_container)
