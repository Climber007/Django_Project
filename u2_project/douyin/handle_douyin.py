import uiautomator2 as u2
import time
import adbutils, multiprocessing

class Douyin(object):
    def __init__(self, serial="192.168.0.102"):
        # 连接
        self.d = u2.connect(serial)
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
        if time.perf_counter() - self.t0 > 360:  # 3600s
            return True

    def handle_watcher(self):
        # 通知权限
        self.d.watcher.when('//*[@resource-id="com.ss.android.ugc.aweme:id/a4r"]').click()
        # 发现滑动查看更多
        self.d.watcher.when('//*[@text="滑动查看更多"]').click()
        self.d.watcher.when('//*[@text="快速进入TA的个人中心"]').click()
        # 给乐视手机使用的监控器
        self.d.watcher.when('//[@text="允许"]').click()

        self.d.watcher.start(interval=1)

    def get_windowsize(self):
        return self.d.window_size()

    def handle_swipe(self):
        x1 = int(self.size[0] * 0.5)
        y1 = int(self.size[1] * 0.9)
        y2 = int(self.size[1] * 0.15)
        self.d.swipe(x1, y1, x1, y2)


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
                # 可能是做广告；
                else:
                    self.handle_swipe()

                # 判断是否正常进入抖音界面
                if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists and self.d(resourceId="com.ss.android.ugc.aweme:id/u0").exists:
                    # 滑动： 由下向上滑动；
                    self.handle_swipe()

def get_devices():
    # 获取当前操作系统中所连接的移动设备 serial num
    return [d.serial for d in adbutils.adb.device_list()]

def handle_device(serial):
    d = Douyin(serial)
    d.swipe_douyin()

def main():
    # 多进程启动u2去滑动移动设备；
    for i in range(len(get_devices())):
        serial = get_devices()[int(i)]
        p = multiprocessing.Process(target=handle_device, args=(serial,))
        p.start()

if __name__ == '__main__':
    main()

