from elasticsearch import Elasticsearch


# Create Index#

# es = Elasticsearch()
# result = es.indices.create(index='news', ignore=400)
# print(result)

# Delete Index#
# es = Elasticsearch()
# result = es.indices.delete(index='news', ignore=[400,404])
# print(result)

# Insert Data#
# es = Elasticsearch()
# es.indices.create(index='zmc', ignore=400)

# data = {'title': 'title123', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
# result = es.index(index = 'zmc', doc_type = 'politics', body = data)
# print(result)

# Update #
es = Elasticsearch()
data = {
    'title': '123456789',
    'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
    'date': '2019-07-23'
}
result = es.update(index = 'news', doc_type = 'politics', body = data, id = 1)
print(result)
