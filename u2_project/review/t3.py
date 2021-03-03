
import pymongo

db_configs = {
    'type': 'mongo',
    'host': '地址',
    'port': '端口',
    'user': 'spider_data',
    'passwd': '密码',
    'db_name': 'spider_data'
}


class Mongo():
    def __init__(self, db=db_configs["db_name"], username=db_configs["user"],
                 password=db_configs["passwd"]):
        self.client = pymongo.MongoClient(f'mongodb://{db_configs["host"]}:db_configs["port"]')
        self.username = username
        self.password = password
        if self.username and self.password:
            self.db1 = self.client[db].authenticate(self.username, self.password)
        self.db1 = self.client[db]

    def find_data(self):
        # 获取状态为0的数据
        data = self.db1.test.find({"status": 0})
        gen = (item for item in data)
        return gen

if __name__ == '__main__':
    m = Mongo()
    print(m.find_data())