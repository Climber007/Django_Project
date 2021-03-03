import time
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(hosts="192.168.0.103:9200")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("耗时{:.3f}".format(time.time()-start_time))
        return res

    return wrapper

@timer
def handle_es():
    for value in range(10000):
        yield {"_index":"value_demo", "_source":{"value":value}}

if __name__ == '__main__':
    helpers.bulk(es, actions=handle_es())



curl -H 'Content-Type: application/x-ndjson' -XPOST '192.168.0.103:9200/_bulk?pretty' --data-binary @logs.jsonl