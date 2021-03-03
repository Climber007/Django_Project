# threading pool

import threading
from concurrent import futures
import logging
import time

# 输出格式定义
FORMAT = '%(asctime)-15s\t [%(processName)s:%(threadName)s, %(process)d:%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

def worker(n):
    logging.info('begin to work{}'.format(n))
    time.sleep(5)
    logging.info('finished{}'.format(n))

# 创建线程池执行器，池的容量为3
executor = futures.ThreadPoolExecutor(max_workers=3)

fs = []   # 任务集合管理
for i in range(3):
    future = executor.submit(worker, i)
    fs.append(future)

while True:
    time.sleep(2)
    logging.info(threading.enumerate())

    flag = True
    for f in fs: #
        logging.info(f.done())
        flag = flag and f.done()

    if flag:
        executor.shutdown() # 清理池，池中线程全部杀掉
        logging.info(threading.enumerate())
        break