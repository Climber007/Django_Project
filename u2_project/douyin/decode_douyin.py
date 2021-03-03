# 特别数据
# 在新版本的抖音，我们是找到的是加密的数据返回；

# 个人信息页接口
# https://aweme-eagle.snssdk.com/aweme/v1/user/?user_id

# 滑动视频接口
# https://aweme-eagle.snssdk.com/aweme/v1/feed


import json

def response(flow):
    """解析10版本抖音app返回数据"""
    # 视频
    if 'https://aweme-eagle.snssdk.com/aweme/v1/feed' in flow.request.url:
        # 使用json来loads response.text
        video_response = json.loads(flow.response.text)
        video_list = video_response.get("aweme_list", [])
        for item in video_list:
            print(item.get("desc"), "")   # 视频标题

    # 发布者页面
    if 'https://aweme-eagle.snssdk.com/aweme/v1/user/?user_id' in flow.request.url:
        person_response = json.loads(flow.response.text)
        person_info = person_response.get("user", "")
        if person_info:
            info = {
                'nickname': person_info.get("nickname", ""),   # 名称
                'total_favorited': person_info.get("total_favorited", 0),  # 点赞数
                'following_count': person_info.get("following_count", 0),  # 关注着数量
                'douyin_id': person_info.get("unique_id", ""),               # 抖音ID
                'folllower_count': person_info.get("follower_count", 0)    # 粉丝数量
            }
            print('--------------------------------------------------------------------')
            print(info)
