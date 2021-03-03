from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="192.168.0.103:9200")
# print(es.ping(), es.info())
# 创建索引
# es.indices.create(index="imooc")
# 查看索引
# print(es.cat.indices())
# 删除索引
# print(es.indices.delete(index="imooc"))
#
# 创建索引并插入数据
# print(es.index(index="imooc", body={"name":"大壮", "age":18}))
# 查询数据
# print(es.search(index="imooc"))
#
# 指定ID创建索引并插入数据
# print(es.index(index="imooc", body={"name":"张三", "age":20}, id=1))
# 查询所有数据
# print(es.search(index="imooc"))
#
# 查询单条数据
# print(es.get(index="imooc", id=1))
#
# search查询SDL单条数据
# print(es.search({
#     "query": {
#         "match":{
#             "name": "大壮"
#         }
#     }
# }))

# 数据的更新
# body = {
#     "doc":{
#         "tags":"imooc"
#     }
# }
# print(es.get(index="imooc", id=1))
# print(es.update(index="imooc", id=1, body=body))
# print(es.get(index="imooc", id=1))

# 单条数据的删除
print(es.delete(index="imooc", id=1))