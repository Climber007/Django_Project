import uiautomator2 as u2

class HandleKaoyanbang(object):
    def __init__(self, serial="192.168.0.100"):
        self.d = u2.connect(serial)
        self.size = self.get_windowsize()
        self.handle_watcher()

    def handle_watcher(self):
        # 用户协议
        self.d.watcher.when('//*[@resource-id="com.tal.kaoyan:id/tip_commit"]').click()
        # 跳过广告
        self.d.watcher.when('//*[@resource-id="com.tal.kaoyan:id/tv_skip"]').click()

        # 监控器要 start启动
        self.d.watcher.start()

    def get_windowsize(self):
        return self.d.window_size()

    def close_app(self):
        # 监控关闭
        self.d.watcher.stop()
        # 停止考研帮app
        self.d.app_stop("com.tal.kaoyan")
        # 清理缓存
        self.d.app_clear("com.tal.kaoyan")

    def handle_kaoyanbang_app(self):
        self.d.app_start(package_name="com.tal.kaoyan")
        self.d(text='密码登录').click_exists(timeout=10)
        self.d(text="手机号/用户名/通行证").set_text('18326602330')
        self.d.xpath('//*[@resource-id="com.tal.kaoyan:id/kylogin_unamelogin_operate_layout"]/android.widget.RelativeLayout[1]').set_text('ls7646001')
        self.d(resourceId="com.tal.kaoyan:id/login_login_btn").click_exists()

        if self.d.wait_activity("com.tal.kaoyan.ui.activity.HomeTabActivity",timeout=10):
            self.d(text="研讯").click_exists(timeout=10)
            # 获取屏幕的中心点 x轴
            # 获取到y轴远方点， 获取到y轴近点；
            x1 = int(self.size[0]*0.5)
            y1 = int(self.size[1]*0.9)
            y2 = int(self.size[1]*0.15)
            while True:
                # get toast 信息提示操作；
                if self.d.toast.get_message(0) == "内容已经全部加载完了":
                    self.close_app()
                    return

                # 开始滑动研讯
                self.d.swipe(x1, y1, x1, y2)


if __name__ == '__main__':
    k = HandleKaoyanbang()
    k.handle_kaoyanbang_app()