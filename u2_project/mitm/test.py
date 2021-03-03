from mitmproxy import ctx

# 必须这么写
def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))  # 灰色
    ctx.log.info(str(flow.request.url))  # 灰色
    ctx.log.info(str(flow.request.host))  # 灰色
    ctx.log.info(str(flow.request.method))  # 灰色
    ctx.log.info(str(flow.request.path))  # 灰色
    # ctx.log.warn(str(flow.request.headers))  # 黄色
    # ctx.log.error(str(flow.request.headers)) # 红色

def response(flow):
    ctx.log.error(str(flow.response.status_code))
    ctx.log.error(str(flow.response.text))