import uiautomator2 as u2
import time

class Douyin(object):
    def __init__(self, serial="192.168.0.102"):
        # 连接
        self.d = u2.connect(serial)
        self.d.service("uiautomator").start()
        # 调用方法
        self.start_app()        # 启动
        self.handle_watcher()  # 监控器
        self.size = self.get_windowsize()
        # 获取初始时间
        self.t0 = time.perf_counter()

    def start_app(self):
        self.d.app_start(package_name="com.ss.android.ugc.aweme")

    def stop_app(self):
        """退出逻辑"""
        self.d.watcher.stop()
        self.d.app_stop("com.ss.android.ugc.aweme")
        self.d.app_clear("com.ss.android.ugc.aweme")

    def stop_time(self):
        if time.perf_counter() - self.t0 > 86400:  # 86400s
            return True

    def handle_watcher(self):
        # 通知权限
        self.d.watcher.when('//*[@resource-id="com.ss.android.ugc.aweme:id/a4r"]').click()
        # 发现滑动查看更多
        self.d.watcher.when('//*[@text="滑动查看更多"]').click()
        self.d.watcher.when('//*[@text="快速进入TA的个人中心"]').click()
        self.d.watcher.start(interval=1)

    def get_windowsize(self):
        return self.d.window_size()


    def swipe_douyin(self):
        '''滑动抖音短视频 点击视频发布者头像的操作'''
        # 判断是否正常进入抖音界面
        if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists(timeout=20):
            while True:
                if self.stop_time():
                    self.stop_app()
                    return

                # 查看 是不是正常的发布者（不是广告）
                if self.d(resourceId="com.ss.android.ugc.aweme:id/u0").exists:
                    # 是不是正常的 发布者，点击头像
                    self.d(resourceId="com.ss.android.ugc.aweme:id/tw").click()
                    # 返回
                    self.d(resourceId="com.ss.android.ugc.aweme:id/et").click()

                # 判断是否正常进入抖音界面
                if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists:
                    # 滑动： 由下向上滑动；
                    x1 = int(self.size[0]*0.5)
                    y1 = int(self.size[1]*0.9)
                    y2 = int(self.size[1]*0.15)
                    self.d.swipe(x1, y1, x1, y2)

if __name__ == '__main__':
    d = Douyin()
    d.swipe_douyin()