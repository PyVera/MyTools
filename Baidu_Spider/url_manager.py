#url管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  #初始化，set()可以去重
        self.used_urls = set()

    def add_new_url(self, url):  #添加单个url
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  #添加批量新url
        if urls is None or len(urls) == 0:  #或者列表为空
            return
        for url in urls:
            self.add_new_url(url)  #调用添加单个url进行添加

    def has_new_url(self):  #判断是否有新url
        return len(self.new_urls) > 0  #当new_urls的长度>0时，说明有新的url

    def get_new_url(self):
        temp_url = self.new_urls.pop()  #获取新url，并移除
        self.used_urls.add(temp_url)  #被移除的url添加入used_url
        return temp_url
